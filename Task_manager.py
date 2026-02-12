import json
from Models import Task
from Project_manager import ProjectManager

class TaskManager:
    FILE = "data/tasks.json"

    def __init__(self):
        self.tasks = self.load()
        self.project_manager = ProjectManager()

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, project, title, description, priority):
        # Titel mag niet leeg zijn
        if not title.strip():
            print("Taaktitel mag niet leeg zijn")
            return

        # Beschrijving mag niet leeg zijn
        if not description.strip():
            print("Beschrijving mag niet leeg zijn")
            return

        # Prioriteit moet geldig zijn
        valid_priorities = ["laag", "medium", "hoog"]
        if priority.lower() not in valid_priorities:
            print("Prioriteit moet 'laag', 'medium' of 'hoog' zijn")
            return

        # Project moet bestaan
        if not any(p["name"].lower() == project.lower() for p in self.project_manager.projects):
            print(f"Project '{project}' bestaat niet")
            return

        # Titel moet uniek zijn binnen hetzelfde project
        for t in self.tasks:
            if (
                t["project"].lower() == project.lower()
                and t["title"].lower() == title.lower()
            ):
                print(f"Er bestaat al een taak met de titel '{title}' in project '{project}'")
                return

        # Nieuw ID bepalen
        new_id = max([t["id"] for t in self.tasks], default=0) + 1

        # Taak aanmaken
        task = Task(
            id=new_id,
            project=project,
            title=title,
            description=description,
            priority=priority.lower(),
            status="open"
        ).__dict__

        self.tasks.append(task)
        self.save()

        print(f"Taak '{title}' toegevoegd aan project '{project}'")

    def list_tasks(self, project):
        # Project moet bestaan
        if not any(p["name"].lower() == project.lower() for p in self.project_manager.projects):
            print(f"Project '{project}' bestaat niet")
            return

        project_tasks = [
            t for t in self.tasks
            if t["project"].lower() == project.lower()
        ]

        if not project_tasks:
            print(f"Geen taken gevonden voor project '{project}'")
            return

        for t in project_tasks:
            status_icon = "✓" if t["status"] == "afgerond" else " "
            print(f"[{status_icon}] {t['id']}: {t['title']} ({t['priority']})")
            print(f"    Beschrijving: {t['description']}")
            print(f"    Status: {t['status']}")
            print(f"    Aangemaakt op: {t['created_at']}\n")

    def mark_done(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["status"] = "afgerond"
                self.save()
                print(f"Taak {task_id} is afgerond")
                return

        print(f"Taak met ID {task_id} bestaat niet")

    def remove_task(self, task_id):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]

        if len(self.tasks) == before:
            print(f"Taak met ID {task_id} bestaat niet")
            return

        self.save()
        print(f"Taak {task_id} verwijderd")