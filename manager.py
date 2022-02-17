import sqlite3 as sqll


class Manager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        if not self.db_name.endswith('.db'):
            self.db_name += '.db'

    def __generate_inserts(self, objs: list, table_name: str,
                           ignore=[], renames_col={}):
        inserts = list()
        for obj in objs:
            sql = f'INSERT INTO {table_name} '
            cols = '('
            values = '('

            attributes = obj.__dict__

            for attr in attributes:
                if attributes[attr] and attr not in ignore:
                    values += '\'' + str(attributes[attr]) + '\', '
                    if attr in renames_col:
                        attr = renames_col[attr]
                    cols += attr + ', '
            sql += cols[:len(cols) - 2] + ') VALUES '
            sql += values[:len(values) - 2] + ')'

            inserts.append(sql)
        return inserts

    def random(self, count=1):
        return list()

    def generate_random_inserts(self, table_name: str, count=1,
                                ignore=[], renames_col={}):
        objs = self.random(count=count)
        return self.__generate_inserts(objs, table_name,
                                       ignore=ignore,
                                       renames_col=renames_col)

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
