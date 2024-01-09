import asyncio
from ctypes import util
from aiogram import Bot, Dispatcher
from utils import fst
from handlers import user_commands, handlers
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.happy_birthday import print_happy_birthday
from utils.commands import set_commands
scheduler = AsyncIOScheduler()

token = "6451631033:AAEE0UZyYoRAYnYwRR22R2pdzpTLtqGPkqI"


async def main():
    bot = Bot(token=token, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(user_commands.router, handlers.router, fst.router)
    scheduler.start()
    scheduler.add_job(print_happy_birthday, "cron", hour=8, kwargs={"bot": bot})
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
