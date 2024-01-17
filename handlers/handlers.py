from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from database.bd import Database
from keyboards.inline import filial_ikey, filial_menu_ikey
router = Router()

db = Database('database\database.db')


@router.message(CommandStart())
async def bot_command_start(message: Message):
    if db.user_exists(message.from_user.id):
        await message.answer("Уже нажимал стар!")
    else:
        db.add_user(message.from_user.id, message.from_user.full_name)
        await message.answer(f"Добро пожаловать {message.from_user.full_name}")
        

# @router.message(F.text == "my")
# async def post_test(message: Message):
#     db.add_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name)  

@router.message(F.text == "test") 
async def get_users_exists(message: Message):
    if db.user_exists(message.from_user.id):
        await message.answer("В таблице!")
    else:
        await message.answer("введи my")

@router.message(F.text == "/filial")
async def inline_key(message: Message):
    await message.answer("Выбери филиал", reply_markup=filial_ikey)


