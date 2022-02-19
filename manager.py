import sqlite3 as sqll


class Manager:
    def __init__(self, db_name: str, table_name: str):
        self.db_name = db_name
        self.table_name = table_name
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

    def generate_random_inserts(self, count=1, ignore=[], renames_col={}):
        objs = self.random(count=count)
        return self.__generate_inserts(objs, self.table_name,
                                       ignore=ignore,
                                       renames_col=renames_col)

    def __do_inserts(self, inserts: list):
        errors = {}
        succ = 0
        try:
            connection = sqll.connect(self.db_name)
            cursor = connection.cursor()

            for i in range(len(inserts)):
                try:
                    cursor.execute(inserts[i])
                    succ += 1
                except sqll.Error as error:
                    if str(error) in errors:
                        errors[str(error)] += 1
                    else:
                        errors[str(error)] = 1
            connection.commit()
            cursor.close()
        except sqll.Error as error:
            if str(error) in errors:
                errors[str(error)] += 1
            else:
                errors[str(error)] = 1
            print('Error:', error)
        finally:
            if connection:
                connection.close()
        return succ, errors

    def do_random_inserts(self, count=1, ignore=[], renames_col={}):
        return self.__do_inserts(self.generate_random_inserts(
                        count,
                        ignore=ignore,
                        renames_col=renames_col))

    def get_objects(self, tablename: str, cols=None, toplimit=None):
        record = []
        try:
            connection = sqll.connect(self.db_name)
            cursor = connection.cursor()

            query = 'SELECT '
            if cols:
                query += ', '.join(cols)
            else:
                query += '*'

            query += f' FROM {tablename}'

            cursor.execute(query)
            record = cursor.fetchall()
            if toplimit:
                record = record[:toplimit]
            cursor.close()
        except sqll.Error as error:
            print('Error:', error)
        finally:
            if connection:
                connection.close()

            return record

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

