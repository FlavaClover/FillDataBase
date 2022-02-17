from datetime import datetime
from manager import Manager
from mimesis import Person, Datetime
from mimesis.enums import Gender


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
    def __init__(self, db_name: str):
        super().__init__(db_name)

    def random(self, count=1):
        person = Person('ru')
        dt_time = Datetime()

        workers = list()
        for _ in range(count):
            workers.append(Worker(
                person.full_name(gender=Gender.MALE),
                None,
                dt_time.date(start=1900, end=2021)
            ))

        return workers
