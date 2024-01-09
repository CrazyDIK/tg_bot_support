from aiogram.types import(
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters.callback_data import CallbackData

filial_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="KBF", callback_data="KBF"),
        InlineKeyboardButton(text="KRF", callback_data="KRF"),
        InlineKeyboardButton(text="LPF", callback_data="LPF")
        ],
        [InlineKeyboardButton(text="MSK", callback_data="MSK"),
        InlineKeyboardButton(text="ORF", callback_data="ORF"),
        InlineKeyboardButton(text="TMF", callback_data="TMF")
        ]
    ]
)