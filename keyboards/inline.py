from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

filial_ikey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="KBF", callback_data="KBF_call_data"),
            InlineKeyboardButton(text="KRF", callback_data="KRF_call_data"),
            InlineKeyboardButton(text="LPF", callback_data="LPF_call_data"),
        ],
        [
            InlineKeyboardButton(text="MSK", callback_data="MSK_call_data"),
            InlineKeyboardButton(text="ORF", callback_data="ORF_call_data"),
            InlineKeyboardButton(text="TMF", callback_data="TMF_call_data"),
        ],
    ]
)

filial_menu_ikey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Info", url="https://agrogard.ru/branches/4.html"),
            InlineKeyboardButton(
                text="IT_Support", callback_data="IT_Support_call_data"
            ),
            InlineKeyboardButton(text="🔙Назад", callback_data="Back_filial",)
        ]
    ]
)

sex_ikey = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Man", callback_data="Man_call_data"),
            InlineKeyboardButton(text="Woman", callback_data="Woman_call_data"),
        ]
    ]
)
