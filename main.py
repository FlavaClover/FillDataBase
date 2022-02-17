from worker import Worker, WorkerManager
from department import Department, DepartmentManager
from manager import Manager
from datetime import datetime


DB_NAME = 'data_base'


if __name__ == "__main__":
    d_manager = DepartmentManager(DB_NAME)

    depts = d_manager.generate_random_inserts(
            'departments', count=1000,
            renames_col={'id_dept': 'id', 'name': 'name_dept'})
    for i in depts:
        print(i)


