#-1004330102800

import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
# 替換為你的群組 Chat ID（注意負號）
GROUP_CHAT_ID = "-1004330102800"

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)

    # 先取得最近的更新，確認正確的 chat_id
    updates = await bot.get_updates()
    if updates:
        for update in updates:
            chat = update.effective_chat
            if chat:
                print(f"Chat 名稱: {chat.title or chat.username or chat.first_name}, Chat ID: {chat.id}")
    else:
        print("⚠️ 沒有收到任何更新，請先在群組內傳一則訊息給 Bot，再重新執行。")
        return
    
    # 主動發送文字訊息給群組
    await bot.send_message(
        chat_id=GROUP_CHAT_ID,
        text="📢 大家好！這是來自機器人的主動推播通知。"
    )
    print("✅ 訊息發送成功！")

if __name__ == "__main__":
    asyncio.run(main())