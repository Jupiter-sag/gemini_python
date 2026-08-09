"""
Gemini API 綜合練習案例
涵蓋：基本文字生成、系統提示、多輪對話、串流輸出、結構化輸出
"""

import os
import google.generativeai as genai

# ── 初始化 ─────────────────────────────────────────────
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"


# ══════════════════════════════════════════════════════
# 1. 基本文字生成
# ══════════════════════════════════════════════════════
def demo_basic_generation():
    print("\n" + "=" * 50)
    print("【1】基本文字生成")
    print("=" * 50)

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content("用三句話介紹台灣的夜市文化")

    print(response.text)
    print(f"\n→ 使用 token 數：{response.usage_metadata.total_token_count}")


# ══════════════════════════════════════════════════════
# 2. 系統提示（System Instruction）
# ══════════════════════════════════════════════════════
def demo_system_instruction():
    print("\n" + "=" * 50)
    print("【2】系統提示")
    print("=" * 50)

    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=(
            "你是一位專業的台灣歷史老師，"
            "回答時請使用繁體中文，並以條列式呈現重點。"
        ),
    )

    response = model.generate_content("簡介台灣日治時期的三件重要事件")
    print(response.text)


# ══════════════════════════════════════════════════════
# 3. 串流輸出（Streaming）
# ══════════════════════════════════════════════════════
def demo_streaming():
    print("\n" + "=" * 50)
    print("【3】串流輸出")
    print("=" * 50)

    model = genai.GenerativeModel(MODEL_NAME)
    stream = model.generate_content(
        "寫一首關於秋天的短詩（四行）",
        stream=True,
    )

    print("逐字輸出：")
    for chunk in stream:
        print(chunk.text, end="", flush=True)
    print()  # 換行


# ══════════════════════════════════════════════════════
# 4. 多輪對話（Multi-turn Chat）
# ══════════════════════════════════════════════════════
def demo_multi_turn_chat():
    print("\n" + "=" * 50)
    print("【4】多輪對話")
    print("=" * 50)

    model = genai.GenerativeModel(MODEL_NAME)
    chat = model.start_chat(history=[])

    turns = [
        "我想學習 Python，從哪裡開始比較好？",
        "你提到的第一個建議，可以給我一個具體的練習題嗎？",
        "這個練習題的參考答案是什麼？",
    ]

    for user_msg in turns:
        print(f"\n👤 使用者：{user_msg}")
        response = chat.send_message(user_msg)
        print(f"🤖 Gemini：{response.text}")

    # 顯示對話歷史長度
    print(f"\n→ 對話共 {len(chat.history)} 輪")


# ══════════════════════════════════════════════════════
# 5. 生成設定（Generation Config）
# ══════════════════════════════════════════════════════
def demo_generation_config():
    print("\n" + "=" * 50)
    print("【5】生成設定：控制溫度與長度")
    print("=" * 50)

    model = genai.GenerativeModel(MODEL_NAME)

    config = genai.types.GenerationConfig(
        temperature=0.2,      # 低溫度 → 回答更精確、一致
        max_output_tokens=150,
        top_p=0.9,
    )

    response = model.generate_content(
        "列出五個 Python 內建函式，並各用一句話說明",
        generation_config=config,
    )
    print(response.text)


# ══════════════════════════════════════════════════════
# 6. 安全設定（Safety Settings）
# ══════════════════════════════════════════════════════
def demo_safety_settings():
    print("\n" + "=" * 50)
    print("【6】安全設定")
    print("=" * 50)

    from google.generativeai.types import HarmCategory, HarmBlockThreshold

    model = genai.GenerativeModel(MODEL_NAME)

    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }

    response = model.generate_content(
        "介紹一部有深度的台灣電影",
        safety_settings=safety_settings,
    )
    print(response.text)
    print(f"\n→ 安全評分：{response.prompt_feedback}")


# ══════════════════════════════════════════════════════
# 主程式
# ══════════════════════════════════════════════════════
def main():
    print("🚀 Gemini API 綜合練習")
    print(f"   使用模型：{MODEL_NAME}")

    demos = [
        ("基本文字生成",   demo_basic_generation),
        ("系統提示",       demo_system_instruction),
        ("串流輸出",       demo_streaming),
        ("多輪對話",       demo_multi_turn_chat),
        ("生成設定",       demo_generation_config),
        ("安全設定",       demo_safety_settings),
    ]

    for name, func in demos:
        try:
            func()
        except Exception as e:
            print(f"\n⚠️  [{name}] 發生錯誤：{e}")

    print("\n\n✅ 所有示範完成")


if __name__ == "__main__":
    main()
