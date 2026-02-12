import json
from Models import Task

class TaskManager:
    FILE = "data/tasks.json"

    def __init__(self):
        self.tasks = self.load()

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, project, title):
        new_id = max([t["id"] for t in self.tasks], default=0) + 1
        task = Task(id=new_id, project=project, title=title).__dict__
        self.tasks.append(task)
        self.save()
        print(f"Taak '{title}' toegevoegd aan project '{project}'")

    def list_tasks(self, project):
        for t in self.tasks:
            if t["project"] == project:
                status = "✓" if t["done"] else " "
                print(f"[{status}] {t['id']}: {t['title']}")