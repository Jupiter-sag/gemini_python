## shopping_board_channel

import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode

load_dotenv()
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# 設定推播目標
TARGET_USER_ID = 8652886039
TARGET_GROUP_ID = -1004330102800
TARGET_CHANNEL_ID = -1004408821186

async def send_photo_broadcast(
    chat_id: str | int,
    photo_source: str,
    caption: str,
    keyboard: InlineKeyboardMarkup | None = None
):
    """
    發送帶有排版說明的圖片推播
    :param photo_source: 圖片網址 (URL) 或 本地圖片路徑
    :param caption: 說明文字 (上限 1024 字元)
    :param keyboard: 訊息底部的按鈕 (選填)
    """
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        # 若傳入本地檔案路徑，以二進位讀取發送；若為 URL 則直接傳入字串
        if os.path.exists(photo_source):
            with open(photo_source, "rb") as photo_file:
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=photo_file,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                    reply_markup=keyboard
                )
        else:
            await bot.send_photo(
                chat_id=chat_id,
                photo=photo_source,
                caption=caption,
                parse_mode=ParseMode.HTML,
                reply_markup=keyboard
            )
        print(f"✅ 成功發送圖文至：{chat_id}")
    except Exception as e:
        print(f"❌ 發送至 {chat_id} 失敗：{e}")

async def main():
    # 1. 圖片來源（使用本地圖片，路徑相對於此腳本所在目錄）
    image_url = os.path.join(os.path.dirname(__file__), "retinol_A.png")

    # 2. HTML 排版內文 (注意：caption 限制上限 1024 字元)
    caption_text = (
        "🔥 <b>【限時下殺】Life-flo, 視黃醇 A 1%，高級煥活乳霜！</b>\n\n"
        "專櫃熱銷爆款，限量釋出只有 3 瓶！\n\n"
        "▫️ <b>改善皮膚：</b> 老化與細紋， 乾燥與缺水\n"
        "▫️ <b>專櫃售價：</b> <s>NT$ 5,000</s>\n"
        "▫️ <b>骨折特價：</b> <b>NT$ 1,800</b> 💥\n\n"
        "<i>完整包裝，提供正品檢驗保證。</i>\n\n"
        "#精品特賣 #Ａ醇 #Neverfull #限時優惠"
    )

    # 3. 底部互動按鈕 (選填，可導向客服私訊或外部賣場)
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🛍️ 立即下單", url="https://t.me/boost?c=4408821186"),
            InlineKeyboardButton("💬 聯絡店長", url="https://t.me/boost?c=4408821186")
        ]
    ])

    targets = [
        TARGET_USER_ID,
        TARGET_GROUP_ID,
        TARGET_CHANNEL_ID
    ]

    for chat_id in targets:
        await send_photo_broadcast(chat_id, image_url, caption_text, keyboard)

if __name__ == "__main__":
    asyncio.run(main())