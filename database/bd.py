import sqlite3
from datetime import datetime


def date_convert_text(data):
    return 

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cur = self.connection.cursor()

    def add_user(self, user_id, first_name, last_name):
        with self.connection:
            self.cur.execute(
                "INSERT INTO `users` (`id`, `first_name`, last_name) VALUES (?,?,?)",
                (user_id, first_name, last_name),
            )

    def user_exists(self, user_id):
        with self.connection:
            result = self.cur.execute("SELECT * FROM `users` WHERE `id` = ?", (user_id,)).fetchall()
            return bool(len(result))