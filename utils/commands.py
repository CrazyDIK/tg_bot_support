from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands=[
        BotCommand(
            command="start",
            description="Запуск бота"
        ),
        BotCommand(
            command="help",
            description="Помощь в управлении ботом"
        ),
        BotCommand(
            command="filial",
            description="Выбрать филиал"
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())