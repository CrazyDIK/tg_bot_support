from email import message
from aiogram import Router, F 
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.ststes import FormADM

router = Router()

@router.message(Command("test"))
async def user_profile(message: Message, state: FSMContext):
    await state.set_state(FormADM.first_name)
    await message.answer("Имя пользователя")

@router.message(FormADM.first_name)
async def form_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(FormADM.last_name)
    await message.answer("Фамилия пользователя")

@router.message(FormADM.last_name)
async def form_last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(FormADM.date_happy_birthday)
    await message.answer("Дата рождения в формате dd.mm.YYYY")

@router.message(FormADM.date_happy_birthday)
async def form_dr_name(message: Message, state: FSMContext):
    await state.update_data(date_happy_birthday=message.text)
    data=await state.get_data()
    await state.clear()
    formatted_text = []
    [
        formatted_text.append(f"{key}: {value}")
        for key, value in data.items()
    ]
    print(formatted_text)

