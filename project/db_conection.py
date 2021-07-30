import sqlite3
import os
from os import path


class DB_Conector():

    def init(self):
        self.cursor = None
        self.username = str()
        self.user_pass = str()
        self.connection = None

    def connect_db(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "world_all.db")
        conn = sqlite3.connect(db_path)
        self.connection = conn
        cur = conn.cursor()
        self.cursor = cur
