import sqlite3
import db_conection
from country_data import CountryData


class DB_actions():

    def __init__(self):
        self.connection = db_conection.DB_Conector()

    def select_data(self, table, query_params):
        connection = self.connection.create_connection()
        result = connection.cursor().execute(
            f"SELECT * FROM {table} where capital = '{query_params}';").fetchall()
        return result

    def select_all(self, table):
        connection = self.connection.create_connection()
        result = connection.cursor().execute(
            f"SELECT * FROM {table};").fetchall()
        return result

    def insert_data(self, table, json):
        connection = self.connection.create_connection()
        country_data = CountryData()
        index = 0
        for values in json:
            country_data.parse(values)
            connection.cursor().execute(country_data.create_query_to_db(table)).fetchall()
            result = connection.commit()
            index += 1
        return result

    def delete_data(self, table, query_params):
        connection = self.connection.create_connection()
        connection.cursor().execute(
            f'DELETE FROM {table} WHERE id_country = "{query_params}";').fetchall()
        result = connection.commit()
        return result

    def update_data(self, table, new_query_params, query_params):
        connection = self.connection.create_connection()
        connection.cursor().execute(
            f'UPDATE {table} SET id_country = {new_query_params} WHERE name_country = "{query_params}";').fetchall()
        result = connection.commit()
        return result
