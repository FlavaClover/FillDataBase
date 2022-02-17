import sqlite3 as sqll


class Manager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        if not self.db_name.endswith('.db'):
            self.db_name += '.db'

    def generate_inserts(self, objs: list, table_name: str, ignore=[]):
        inserts = list()
        for obj in objs:
            sql = f'INSERT INTO {table_name} '
            cols = '('
            values = '('

            attributes = obj.__dict__

            for attr in attributes:
                if attributes[attr] and attr not in ignore:
                    cols += attr + ', '
                    values += '\'' + str(attributes[attr]) + '\', '
            sql += cols[:len(cols) - 2] + ') VALUES '
            sql += values[:len(values) - 2] + ')'

            inserts.append(sql)
        return inserts

    def check_db(self):
        try:
            connection = sqll.connect(self.db_name)
            cursor = connection.cursor()
            print('Successful connection')

            query = 'SELECT sqlite_version()'
            cursor.execute(query)
            record = cursor.fetchall()

            print('Version:', record)
            cursor.close()
        except sqll.Error as error:
            print('Error:', error)
        finally:
            if connection:
                connection.close()
                print('Connection closed')
