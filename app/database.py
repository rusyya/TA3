import sqlite3
from datetime import datetime
from typing import List, Optional
from .models import Project, Task, ProjectStatus, TaskPriority

class DatabaseManager:
    def __init__(self, db_path: str = "projects.db"):
        self.db_path = db_path
        self._init_database()

    def _init_database(self):
        pass

    def add_project(self):
        pass

    def add_task(self):
        pass

    def del_project(self):
        pass

    def del_task(self):
        pass

    def get_all_projects(self):
        pass

    def get_tasks_by_project(self):
        pass