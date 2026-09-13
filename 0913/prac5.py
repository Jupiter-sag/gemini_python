import os
from enum import Enum
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# 載入環境變數
load_dotenv()

# 1. 定義情緒枚舉與結構化 Schema
class SentimentType(str, Enum):
    POSITIVE = "positive"      # 正向滿意
    NEUTRAL = "neutral"        # 一般詢問 / 中立
    NEGATIVE = "negative"      # 輕微不滿 / 抱怨
    URGENT_ANGRY = "urgent_angry"  # 強烈憤怒 / 要求主管或退費

class SentimentAnalysisResult(BaseModel):
    sentiment: SentimentType = Field(description="用戶訊息的情緒分類")
    confidence_score: float = Field(description="情緒判斷的信心指數 (0.0 到 1.0)")
    requires_human_agent: bool = Field(description="是否需要立即轉接真人客服處理")
    reasoning: str = Field(description="判斷該情緒的簡短理由或關鍵字說明")
    suggested_reply: str = Field(description="適合 Telegram 客服機器人給予該使用者的同理心回覆建議")

# 2. 初始化 Gemini Client
client = genai.Client()

def analyze_customer_message(user_message: str) -> SentimentAnalysisResult:
    system_instruction = """
    你是一位專業的 Telegram 線上客服情緒分析與應對助手。
    請分析客戶發送的訊息情緒，並特別注意台灣在地的口語語境與反諷語氣。
    如果客戶表達強烈不滿、投訴消保官、威脅退費或情緒極度憤怒，請將 requires_human_agent 標記為 True。
    """

    # 3. 呼叫模型並強制使用結構化輸出
    response = client.models.generate_content(
        model="gemini-3.6-flash",  # 最新世代 Flash 速度快、成本低，適合即時客服
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=SentimentAnalysisResult,
            temperature=0.1,  # 降低隨機性以提升分類穩定度
        ),
    )

    # 4. 解析驗證結果（SDK 會自動將 JSON 解析成定義的 Pydantic 物件）
    result: SentimentAnalysisResult = response.parsed
    return result

# 5. 測試執行
if __name__ == "__main__":
    test_messages = [
        "請問我的訂單 #883921 什麼時候會出貨呢？謝謝！",
        "你們的APP到底怎麼回事？一直閃退，付了錢什麼都不能用，再不處理我就找消保官！",
        "包裹收到了，包裝很完整，速度也很快～"
    ]

    for msg in test_messages:
        print(f"\n--- 測試訊息: {msg} ---")
        analysis = analyze_customer_message(msg)
        print(f"情緒標籤: {analysis.sentiment.value}")
        print(f"信心指數: {analysis.confidence_score}")
        print(f"轉接真人: {'是' if analysis.requires_human_agent else '否'}")
        print(f"判斷依據: {analysis.reasoning}")
        print(f"建議回覆: {analysis.suggested_reply}")