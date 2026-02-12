import json
from Models import Project

class ProjectManager:
    FILE = "data/projects.json"

    def __init__(self):
        self.projects = self.load()

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.projects, f, indent=4)

    def add_project(self, name):
        project = Project(name=name).__dict__
        self.projects.append(project)
        self.save()
        print(f"Project '{name}' toegevoegd")