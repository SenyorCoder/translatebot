from aiogram import types
from keyboards.inline.til import language
from loader import dp


@dp.message_handler(commands="lang")
async def bot_help(message: types.Message):
    await message.answer(f"📑 Quyidagi tillardan birini tanlang va tajrima uchun matn yozib qoldiring 👇🏻", reply_markup=language)