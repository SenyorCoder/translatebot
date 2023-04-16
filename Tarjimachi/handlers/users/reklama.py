from aiogram import types

from loader import dp, db


@dp.message_handler(commands='reklama')
async def bot_help(message: types.Message):
    count = db.count_users()
    await message.answer(f"<b>📊 Bot auditoriyasi:</b>\n\n👥<i><b> Obunachilar:</b> </i>{count[0]} ta.\n<i><b>📲 Reklama:</b></i> Hamma obunachiga yuboriladi.\n👁‍🗨<i><b> Obuna bo'l:</b></i> Botga start bosganda kanalga obuna bo'lish qo'shiladi.\n\n👨🏻‍💻 Reklama uchun: @Middle_Developer")