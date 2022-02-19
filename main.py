from worker import Worker, WorkerManager
from department import Department, DepartmentManager
from settings import DEPT_TABLE, DB_NAME, WORKER_TABLE
from manager import Manager
from datetime import datetime


if __name__ == "__main__":
    d_manager = DepartmentManager(DB_NAME, DEPT_TABLE)
    w_manager = WorkerManager(DB_NAME, WORKER_TABLE)

    succ_dept, errors_dept = d_manager.do_random_inserts(count=10)
    succ_worker, errors_worker = w_manager.do_random_inserts(
            count=5,
            renames_col={'date': 'start_date'})

    print(succ_dept + succ_worker)

    print('Department table errors: ')
    for i in errors_dept:
        print(i, errors_dept[i])

    print('Worker table errors:')
    for i in errors_worker:
        print(i, errors_worker[i])
#    depts = d_manager.generate_random_inserts(count=1000)
#
#    objects = d_manager.get_departments(toplimit=10)
#    for i in objects:
#        print(i)

#    w_manager = WorkerManager(DB_NAME, WORKER_TABLE)
#    workers = w_manager.random(count=100000)
#    for i in workers:
#        print(i)
#    

#    succ, errors = d_manager.do_inserts(depts)
#    print(succ)
#    for i in errors:
#        print(i, errors[i])
