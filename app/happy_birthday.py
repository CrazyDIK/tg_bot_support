import asyncio
import csv
from datetime import datetime
from aiogram import Bot


def check_happy_birthday():
    with open("app\happy_birthday.csv", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        dr = []
        for l_dict in reader:
            if datetime.strptime(l_dict["Дата"], "%d.%m.%Y").strftime(
                "%d-%m"
            ) == datetime.now().date().strftime("%d-%m"):
                dr.append(l_dict)
            else:
                pass
        return dr


async def print_happy_birthday(bot: Bot):
    for dr in check_happy_birthday():
        await bot.send_message(
            1053526748,
            f"Уважаемый {dr['Имя']} {dr['Отчество']}!\n"
            f"АО АгроГрад поздравляет с днем рождения\n"
            f"и искренне желает счатья и процветания.🎂,"
        )
