from aiogram import types, bot
from aiogram.types import CallbackQuery
from keyboards.inline.news import yangilik
from loader import dp
from tarjimon import tar, ara, arauz, uzrus, rusuz
from aiogram.dispatcher import FSMContext
from uztarjimon import uzbcha

## ENG TO UZB

@dp.callback_query_handler(text="birr")
async def cal(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"<i><b>Ingliz</b> tilidan <b>O'zbek</b> tiliga tarjima qilish uchun matn "
                                        f"yuboring</i>👇🏻")
    await state.set_state('tiltan')
    await call.message.delete()

@dp.message_handler(state='tiltan')
async def mes(message: types.Message, state: FSMContext):
    kutish = await message.answer_sticker(
            "CAACAgIAAxkBAAEIljBkOkMzxE-bswfnwmMYSEnxmxitwQACwQoAAh5hoUpZi8YqzCzJ5S8E")
    natija = tar(message.text)
    await message.reply(f"{natija}\n\n<i>Tilni o'zgartirish uchun</i>👉🏻 /lang", reply_markup=yangilik)
    await kutish.delete()
    await state.finish()

## UZB TO ENG

@dp.callback_query_handler(text="ikkii")
async def cal(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"<i><b>O'zbek</b> tilidan <b>Ingliz</b> tiliga tarjima qilish uchun matn "
                                        f"yuboring</i>👇🏻")
    await state.set_state(state='uztil')
    await call.message.delete()

@dp.message_handler(state='uztil')
async def mess(message: types.Message, state: FSMContext):
    kutish = await message.answer_sticker("CAACAgIAAxkBAAEIljBkOkMzxE-bswfnwmMYSEnxmxitwQACwQoAAh5hoUpZi8YqzCzJ5S8E")
    natija = uzbcha(message.text)
    await message.reply(f"{natija}\n\n<i>Tilni o'zgartirish uchun</i>👉🏻 /lang", reply_markup=yangilik)
    await kutish.delete()
    await state.finish()

## UZB TO ARB

@dp.callback_query_handler(text="olti")
async def cal(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"<i><b>O'zbek</b> tilidan <b>Arab</b> tiliga tarjima qilish uchun matn "
                                        f"yuboring</i>👇🏻")
    await state.set_state(state='artil')
    await call.message.delete()

@dp.message_handler(state='artil')
async def mess(message: types.Message, state: FSMContext):
    kutish = await message.answer_sticker("CAACAgIAAxkBAAEIljBkOkMzxE-bswfnwmMYSEnxmxitwQACwQoAAh5hoUpZi8YqzCzJ5S8E")
    arnatija = ara(message.text)
    await message.reply(f"{arnatija}\n\n<i>Tilni o'zgartirish uchun</i>👉🏻 /lang", reply_markup=yangilik)
    await kutish.delete()
    await state.finish()

## RUS TO UZB

@dp.callback_query_handler(text="uch")
async def cal(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"<i><b>Rus</b> tilidan <b>O'zbek</b> tiliga tarjima qilish uchun matn "
                                        f"yuboring</i>👇🏻")
    await state.set_state(state='ruuzutil')
    await call.message.delete()

@dp.message_handler(state='ruuzutil')
async def mess(message: types.Message, state: FSMContext):
    kutish = await message.answer_sticker("CAACAgIAAxkBAAEIljBkOkMzxE-bswfnwmMYSEnxmxitwQACwQoAAh5hoUpZi8YqzCzJ5S8E")
    ruuznatija = rusuz(message.text)
    await message.reply(f"{ruuznatija}\n\n<i>Tilni o'zgartirish uchun</i>👉🏻 /lang", reply_markup=yangilik)
    await kutish.delete()
    await state.finish()


## UZB TO RUS

@dp.callback_query_handler(text="torr")
async def cal(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"<i><b>O'zbek</b> tilidan <b>Rus</b> tiliga tarjima qilish uchun matn "
                                        f"yuboring</i>👇🏻")
    await state.set_state(state='uzrutil')
    await call.message.delete()

@dp.message_handler(state='uzrutil')
async def mess(message: types.Message, state: FSMContext):
    kutish = await message.answer_sticker("CAACAgIAAxkBAAEIljBkOkMzxE-bswfnwmMYSEnxmxitwQACwQoAAh5hoUpZi8YqzCzJ5S8E")
    uzrunatija = uzrus(message.text)
    await message.reply(f"{uzrunatija}\n\n<i>Tilni o'zgartirish uchun</i>👉🏻 /lang", reply_markup=yangilik)
    await kutish.delete()
    await state.finish()


## UZB TO KOR

@dp.callback_query_handler(text="besh")
async def cal(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"<i><b>O'zbek</b> tilidan <b>Koreys</b> tiliga tarjima qilish uchun matn "
                                        f"yuboring</i>👇🏻")
    await state.set_state(state='autil')
    await call.message.delete()

@dp.message_handler(state='autil')
async def mess(message: types.Message, state: FSMContext):
    kutish = await message.answer_sticker("CAACAgIAAxkBAAEIljBkOkMzxE-bswfnwmMYSEnxmxitwQACwQoAAh5hoUpZi8YqzCzJ5S8E")
    aunatija = arauz(message.text)
    await message.reply(f"{aunatija}\n\n<i>Tilni o'zgartirish uchun</i>👉🏻 /lang", reply_markup=yangilik)
    await kutish.delete()
    await state.finish()