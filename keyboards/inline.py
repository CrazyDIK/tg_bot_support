from aiogram.types import(
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters.callback_data import CallbackData

filial_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="KBF", callback_data="KBF_call_data"),
        InlineKeyboardButton(text="KRF", callback_data="KRF_call_data"),
        InlineKeyboardButton(text="LPF", callback_data="LPF_call_data")
        ],
        [InlineKeyboardButton(text="MSK", callback_data="MSK_call_data"),
        InlineKeyboardButton(text="ORF", callback_data="ORF_call_data"),
        InlineKeyboardButton(text="TMF", callback_data="TMF_call_data")
        ]
    ]
)

filial_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Info", callback_data="Info_call_data"),
        InlineKeyboardButton(text="IT_Support", callback_data="IT_Support_call_data"),
        InlineKeyboardButton(text="🔙Назад", callback_data="Back_filial")
        ]
    ]
)
