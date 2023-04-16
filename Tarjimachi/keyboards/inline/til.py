from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from loader import dp

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧Eng 👉🏻 Uzb🇺🇿", callback_data='birr'),
            InlineKeyboardButton(text="🇺🇿Uzb 👉🏻 Eng🇬🇧", callback_data="ikkii"),
        ],
        [
            InlineKeyboardButton(text="🇷🇺Rus 👉🏻 Uzb🇺🇿", callback_data='uch'),
            InlineKeyboardButton(text="🇺🇿Uzb 👉🏻 Rus🇷🇺", callback_data="torr"),
        ],
        [
            InlineKeyboardButton(text="🇺🇿 Uzb 👉🏻 Kor🇰🇷", callback_data='besh'),
            InlineKeyboardButton(text="🇺🇿Uzb 👉🏻 Arb🇸🇦", callback_data="olti"),
        ],
        [
            InlineKeyboardButton(text="🌐 Boshqa tillar uchun 🌐", url="https://t.me/SenyorCode")
        ]
    ]
)
