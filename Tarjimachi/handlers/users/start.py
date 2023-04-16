import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import Kanal, ADMINS
from keyboards.inline.obunabol import check_button
from keyboards.inline.til import language
from loader import dp, bot, db
from utils.misc import subscribe


@dp.message_handler(CommandStart())
async def show_channel(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass
    channels_format = str()
    for channel in Kanal:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f"<a href='{invite_link}'>{chat.title}</a>\n"
        status = await subscribe.check(user_id=message.from_user.id, channel=channel)
        if status:
            await message.answer(
                f"<i>Tarjima qilmoqchi bo'lgan tilni tanlang</i>👇🏻",
                reply_markup=language)
        else:
            await message.answer(f"<b>Botdan foydalanish uchun, iltimos kanalga obuna bo'ling!👇🏻</b>",
                                 reply_markup=check_button,
                                 disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in Kanal:
        status = await subscribe.check(user_id=call.from_user.id, channel=channel)
        if status:
            result += f"<i>Tarjima qilmoqchi bo'lgan tilni tanlang</i>👇🏻"
            await call.message.delete()
            await call.message.answer(result, reply_markup=language, disable_web_page_preview=True)
        else:
            result += f"<b>Obuna bo'lmagansiz! iltimos kanalga obuna bo'ling.👮🏻‍♂️👆🏻</b>"
            await call.message.answer(result, disable_web_page_preview=True)


# import sqlite3
#
# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
#
# from data.config import ADMINS
# from loader import dp, db, bot
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     name = message.from_user.full_name
#     # Foydalanuvchini bazaga qo'shamiz
#     try:
#         db.add_user(id=message.from_user.id,
#                     name=name)
#     except sqlite3.IntegrityError as err:
#         pass
#
#     await message.answer("Xush kelibsiz!")
#     # Adminga xabar beramiz
#     count = db.count_users()[0]
#     msg = f"{message.from_user.get_mention()} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
#     await bot.send_message(chat_id=ADMINS[0], text=msg)