from sqlite3.dbapi2 import Cursor
import db_conection


class DB_actions():

    def __init__(self):
        self.connection = db_conection.DB_Conector()

    def select_data(self, table, query_params):
        self.connection.connect_db()
        connection = self.connection.connection
        result = connection.execute(
            f"SELECT * FROM {table};")
        connection.commit()
        return result

    def insert_data(self, data_to_insert, table):
        return self.connection.cur(f"insert {data_to_insert} to {table}")
