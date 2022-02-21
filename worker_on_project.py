from worker import Worker, WorkerManager
from project import Project, ProjectManager
from manager import Manager
from settings import DB_NAME, WORKER_TABLE, PROJECT_TABLE
from random import randint


class WorkerOnProject:
    roles = ('Стажер', 'Junior', 'Middle', 'Senior')

    def __init__(self, id_worker: int, id_project: int, role: str):
        self.id_worker = id_worker
        self.id_project = id_project
        self.role = role

    def __str__(self):
        return f'{self.id_worker}|{self.id_project}|{self.role}'

    def __repr__(self):
        return str(self)


class WorkerOnProjectManager(Manager):
    def __init__(self, db_name: str, table_name: str):
        super().__init__(db_name, table_name)

    def random(self, count=1):
        w_manager = WorkerManager(DB_NAME, WORKER_TABLE)
        p_manager = ProjectManager(DB_NAME, PROJECT_TABLE)

        workers_on_projects = list()
        for _ in range(count):
            worker_count, _ = w_manager.get_count()
            workers = w_manager.get_workers(count=worker_count)
            worker = workers[randint(0, worker_count - 1)]

            project_count, _ = p_manager.get_count()
            projects = p_manager.get_projects(count=project_count)
            project = projects[randint(0, project_count - 1)]

            roles = WorkerOnProject.roles
            role = roles[randint(0, len(roles) - 1)]

            wp = WorkerOnProject(worker.id_worker, project.id_project, role)
            workers_on_projects.append(wp)

        return workers_on_projects
