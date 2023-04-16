import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

adss = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bepul E'lon Joylash", url="https://t.me/teleshopuz")
        ]
    ]
)

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(f"{users}\n")

@dp.message_handler(text="/ads", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        # await bot.send_message(chat_id=user_id, text="@SenyoCode kanaliga obuna bo'ling")
        await bot.send_photo(chat_id=user_id, photo="https://im.wampi.ru/2023/04/16/photo_2023-04-16_12-03-06.jpg", caption="<b>📲 TEZ SOTING YOKI ARZON SOTIB OLING!</b>\n\n🔥 Biz bilan <b>OSSON, QULAY </b>VA<b> TEZKOR </b>soting yoki sotib oling. Sizning birinchi e'loningiz reklamasi mutlaqo <b>BEPUL</b> bering!😍\n\n<b>👇🏻| HOZIROQ E'LON BERISH |👇🏻</b>\nhttps://t.me/+D7ak-T6t5t42MmEy\nhttps://t.me/+D7ak-T6t5t42MmEy\nhttps://t.me/+D7ak-T6t5t42MmEy\n<b>👆🏻| HOZIROQ E'LON BERISH |👆🏻</b>\n\n✅ @teleshopuz", parse_mode=types.ParseMode.HTML, reply_markup=adss)
        await asyncio.sleep(0.05)

@dp.message_handler(text="/cleandbnowrite", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")