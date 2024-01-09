import asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    pass
