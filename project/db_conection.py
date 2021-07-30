import sqlite3
import os
from os import path


class DB_Conector():

    def init(self):
        self.username = str()
        self.user_pass = str()
        self.connection = None

    def create_connection(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "world_all.db")
        return sqlite3.connect(db_path)
