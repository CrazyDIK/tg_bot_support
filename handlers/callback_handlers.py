from aiogram import Router, F
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(F.data.startswith("LPF"))
async def lpf_filial(call: CallbackQuery):
    await call.message.answer("Липецкий филиал:")
    await call.answer()