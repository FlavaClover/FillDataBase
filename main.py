from worker import Worker, WorkerManager
from department import Department, DepartmentManager
from project import Project, ProjectManager
from worker_on_project import WorkerOnProject, WorkerOnProjectManager
from settings import (
        DEPT_TABLE,
        DB_NAME,
        WORKER_TABLE,
        PROJECT_TABLE,
        WORKER_ON_PROJECT_TABLE
        )
from manager import Manager
from datetime import datetime


if __name__ == "__main__":
    d_manager = DepartmentManager(DB_NAME, DEPT_TABLE)
    w_manager = WorkerManager(DB_NAME, WORKER_TABLE)
    p_manager = ProjectManager(DB_NAME, PROJECT_TABLE)
    wp_manager = WorkerOnProjectManager(DB_NAME, WORKER_ON_PROJECT_TABLE)

    succ_dept, errors_dept = d_manager.do_random_inserts(count=10)
    succ_worker, errors_worker = w_manager.do_random_inserts(
            count=5,
            renames_col={'date': 'start_date'})
    succ_project, errors_project = p_manager.do_random_inserts(count=7)
    succ_wp, errors_wp = wp_manager.do_random_inserts(count=15)

    print('Successful:', succ_dept + succ_worker + succ_project + succ_wp)

    print('Department table errors: ')
    for i in errors_dept:
        print('\t', i, errors_dept[i])

    print('Worker table errors:')
    for i in errors_worker:
        print('\t'. i, errors_worker[i])

    print('Project table errors:')
    for i in errors_project:
        print('\t'. i, errors_project[i])

    print('Workers on projects table errors:')
    for i in errors_wp:
        print('\t', i, errors_wp[i])

#    w_manager = WorkerManager(DB_NAME, WORKER_TABLE)
#    for i in w_manager.get_workers(count=w_manager.get_count()):
#        print(i)
#
#    p_manager = ProjectManager(DB_NAME, PROJECT_TABLE)
#    for i in p_manager.get_projects(count=p_manager.get_count()):
#        print(i)
#
#    print(i)
#    wp_manager = WorkerOnProjectManager(DB_NAME, WORKER_ON_PROJECT_TABLE)
#    for i in wp_manager.random(count=10):
#        print(i)

