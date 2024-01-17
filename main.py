import asyncio
import os
from ctypes import util
from tokenize import Token
from aiogram import Bot, Dispatcher
from utils import fst
from handlers import callback_handlers, handlers
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.happy_birthday import print_happy_birthday
from utils.commands import set_commands
from dotenv import load_dotenv

load_dotenv()

scheduler = AsyncIOScheduler()

token = os.getenv("TOKEN")


async def main():
    bot = Bot(token=token, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(callback_handlers.router, handlers.router, fst.router)
    scheduler.start()
    scheduler.add_job(print_happy_birthday, "cron", hour=8, minute=15, kwargs={"bot": bot})
    await set_commands(bot)
    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")
