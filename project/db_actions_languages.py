import sqlite3
import db_conection


class DB_actions():

    def __init__(self):
        self.connection = db_conection.DB_Conector()

    def insert_data(self, table, language):
        connection = self.connection.create_connection()
        index = 0
        for values in language:
            index_name = 0
            count_languages = language[index]["languages"]
            for values in count_languages:
                country_languages = language[index]["languages"][index_name]["name"]
                index_name += 1
            index += 1
        return result
