import sqlite3
from datetime import datetime


def date_convert_text(data):
    return 

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, tg_id, user_name):
        with self.connection:
            self.cursor.execute(
                "INSERT INTO `users` (`tg_id`, user_name) VALUES (?,?)",
                (tg_id, user_name),
            )

    def user_exists(self, tg_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `tg_id` = ?", (tg_id,)).fetchall()
            return bool(len(result))
        
    def get_tg_id(self, tg_id):
        with self.connection:
            result = self.cursor.execute("SELECT `id` FROM `users` WHERE `tg_id` = ?", (tg_id,))
            return result.fetchone(0)[0]
        
    