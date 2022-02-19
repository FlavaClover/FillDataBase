from datetime import datetime
from settings import DEPT_TABLE
from manager import Manager
from mimesis import Datetime, Text, Address
from mimesis.enums import Gender


class Department:
    def __init__(self, name: str, town: str,
                 start_date: datetime, id_dept=None):
        self.name = name
        self.town = town
        self.start_date = start_date
        self.id_dept = id_dept

    def __str__(self):
        return f'{self.id_dept}|{self.name}|{self.town}|{self.start_date}'

    def __repr__(self):
        return str(self)


class DepartmentManager(Manager):
    def __init__(self, db_name: str, table_name: str):
        super().__init__(db_name, table_name)

    def random(self, count=1):
        text = Text('ru')
        dt_time = Datetime()
        address = Address('ru')

        departments = list()

        for _ in range(count):
            departments.append(Department(
                text.word(),
                address.city(),
                dt_time.date(start=1996, end=2021))
            )

        return departments

    def get_departments(self, toplimit=None):
        cols = ['id_dept', 'name', 'town', 'start_date']
        depts = self.get_objects(self.table_name,
                                 cols=cols,
                                 toplimit=toplimit)
        depts = [Department(i[1], i[2], i[3], id_dept=i[0]) for i in depts]
        return depts
