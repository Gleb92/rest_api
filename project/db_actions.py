import sqlite3
import db_conection


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

    def insert_data(self, table, country):
        connection = self.connection.create_connection()
        index = 0
        for values in country:
            country_name = country[index]["name"]
            country_capital = country[index]["capital"]
            country_calling_codes = country[index]["callingCodes"][0]
            country_population = country[index]["population"]
            country_area = country[index]["area"]
            country_flag = country[index]["flag"]
            country_capital = country_capital.replace("'", "''")
            country_name = country_name.replace("'", "''")
            connection.cursor().execute(f"INSERT INTO {table} (name_country, capital, callingCodes, population, area, flag) \
                        VALUES ('{country_name}', '{country_capital}', \
                        '{country_calling_codes}', '{country_population}', \
                        '{country_area}','{country_flag}');").fetchall()
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
