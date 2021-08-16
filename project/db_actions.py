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

    def select_all(self, table, table2, table3):
        connection = self.connection.create_connection()
        select_param = f"{table}.id_country, name_country, capital, callingCodes, population, area, flag, {table2}.languages, {table3}.region"
        result = connection.cursor().execute(
            f"SELECT {select_param} FROM {table} INNER JOIN {table2} ON {table2}.id_country = {table}.id_country \
                                 JOIN {table3} ON {table3}.id_country = {table2}.id_country ;").fetchall()
        return result

    def insert_data(self, table, json):
        connection = self.connection.create_connection()
        country_data = CountryData()
        index = 0
        for values in json:
            country_data.parse(values)
            connection.cursor().executescript(country_data.create_query_to_db(table)).fetchall()
            result = connection.commit()
            index += 1
        return result

    def delete_data(self, table, colonum_table, query_params):
        connection = self.connection.create_connection()
        connection.cursor().execute(
            f'DELETE FROM {table} WHERE {colonum_table} = "{query_params}";').fetchall()
        result = connection.commit()
        return result

    def update_data(self, table, new_query_params, query_params):
        connection = self.connection.create_connection()
        connection.cursor().execute(
            f'UPDATE {table} SET id_country = {new_query_params} WHERE name_country = "{query_params}";').fetchall()
        result = connection.commit()
        return result

    def select_all_country(self, country_name):
        connection = self.connection.create_connection()
        table = "country"
        table2 = "language"
        table3 = "location"
        select_param = f"{table}.id_country, name_country, capital, callingCodes, population, area, flag, {table2}.languages, {table3}.region"
        result = connection.cursor().execute(
            f"SELECT {select_param} FROM {table} INNER JOIN {table2} ON {table2}.id_country = {table}.id_country \
                                 JOIN {table3} ON {table3}.id_country = {table2}.id_country WHERE {table}.name_country = '{country_name}';").fetchall()
        return result

    def select_all_country_info(self):
        connection = self.connection.create_connection()
        res = connection.cursor().execute(
            f"SELECT name_country FROM country").fetchall()
        return res
