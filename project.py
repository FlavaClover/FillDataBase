from datetime import datetime
from settings import PROJECT_TABLE, DB_NAME
from manager import Manager
from mimesis import Datetime, Finance
from random import randint


class Project:
    statuses = ('в работе', 'закончен')

    def __init__(self, name: str, start_date: datetime,
                 budget: int, status: str, id_project=None):
        self.name = name
        self.start_date = start_date
        self.budget = budget
        self.id_project = id_project
        self.status = status

    def __str__(self):
        return f'{self.id_project}|{self.name}|{self.start_date}|{self.budget}'

    def __repr__(self):
        return str(self)


class ProjectManager(Manager):
    def __init__(self, db_name: str, table_name: str):
        super().__init__(db_name, table_name)

    def random(self, count=1):
        dt_time = Datetime()
        finance = Finance('ru')

        projects = list()
        for _ in range(count):
            projects.append(Project(finance.company(),
                                    dt_time.date(start=1996, end=2022),
                                    randint(100000, 100000000),
                                    Project.statuses[randint(0, 1)])
                            )
        return projects

    def get_projects(self, count=1):
        cols = ['id_project', 'name', 'start_date', 'budget', 'status']
        projects = self.get_objects(cols=cols, toplimit=count)

        projects = [Project(i[1], i[2], int(i[3]), i[4], id_project=int(i[0])) for i in projects]
        return projects
