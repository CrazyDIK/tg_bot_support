from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline import filial_menu_ikey, filial_ikey

router = Router()


@router.callback_query(F.data.startswith("LPF_call_data"))
async def lpf_filial(call: CallbackQuery):
    await call.message.answer("Липецкий филиал:", reply_markup=filial_menu_ikey)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()


@router.callback_query(F.data.startswith("Back_filial"))
async def lpf_filial(call: CallbackQuery):
    await call.message.answer("Липецкий филиал:", reply_markup=filial_ikey)
    
    await call.answer()


# @router.callback_query(F.data.startswith("Info_call_data"))
# async def lpf_filial(call: CallbackQuery):
#     await call.message.answer(f"Липецкий филиал: \n"
#                               f"22кГа")
#     await call.answer()


# @router.callback_query(F.data.startswith("Info_call_data"))
# async def lpf_Info(call: CallbackQuery):
#     await call.message.answer("")
