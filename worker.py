from datetime import datetime
from settings import DEPT_TABLE, DB_NAME
from manager import Manager
from department import DepartmentManager
from mimesis import Person, Datetime
from mimesis.enums import Gender
from random import randint


class Worker:
    def __init__(self, fullname: str, id_dept: id,
                 start_date: datetime, id_worker=None):
        self.id_worker = id_worker
        self.fullname = fullname
        self.id_dept = id_dept
        self.date = start_date

    def __str__(self):
        return f'{self.id_worker}|{self.fullname}|{self.id_dept}|{self.date}'

    def __repr__(self):
        return str(self)


class WorkerManager(Manager):
    def __init__(self, db_name: str, table_name: str):
        super().__init__(db_name, table_name)

    def random(self, count=1):
        person = Person('ru')
        dt_time = Datetime()
        d_manager = DepartmentManager(DB_NAME, DEPT_TABLE)
        depts = d_manager.get_departments()

        workers = list()
        for _ in range(count):
            workers.append(Worker(
                person.full_name(gender=Gender.MALE),
                depts[randint(0, len(depts) - 1)].id_dept,
                dt_time.date(start=1900, end=2021)
            ))

        return workers

    def get_workers(self, count=1):
        cols = ['id_worker', 'fullname', 'id_dept', 'start_date']
        workers = self.get_objects(cols=cols, toplimit=count)

        workers = [Worker(i[1], int(i[2]), i[3], id_worker=int(i[0])) for i in workers]
        return workers
