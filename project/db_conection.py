import json
import sqlite3
import os
from os import path
import sys


class DB_Conector():

    def init(self):
        self.connection = None
        self.username = str()
        self.user_pass = str()

    def connect_db(self):
        #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        #db_path = os.path.join(BASE_DIR, "world_all.db")
        sys.path.append('rest_api/project')
        #conn = sqlite3.connect()
        sqlite_connection = sqlite3.connect('./world_all.db')
        cur = sqlite_connection.cursor()
        self.connection = cur
