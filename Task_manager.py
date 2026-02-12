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
        if not title.strip():
            print("Taaktitel mag niet leeg zijn")
            return

        if not any(p["name"].lower() == project.lower() for p in self.project_manager.projects):
            print(f"Project '{project}' bestaat niet")
            return

        if any(
            t["project"].lower() == project.lower() and
            t["title"].lower() == title.lower()
            for t in self.tasks
        ):
            print(f"Titel '{title}' bestaat al in '{project}'")
            return

        new_id = max((t["id"] for t in self.tasks), default=0) + 1

        task = Task(
            id=new_id,
            project=project,
            title=title,
            description=description,
            priority=priority,
            status="open"
        ).__dict__

        self.tasks.append(task)
        self.save()
        print(f"Taak '{title}' toegevoegd aan '{project}' (prioriteit: {priority})")

    def list_tasks(self, project):
        if not any(p["name"].lower() == project.lower() for p in self.project_manager.projects):
            print(f"Project '{project}' bestaat niet")
            return

        project_tasks = [t for t in self.tasks if t["project"].lower() == project.lower()]

        if not project_tasks:
            print(f"Geen taken gevonden voor project '{project}'")
            return

        priority_order = {"hoog": 0, "medium": 1, "laag": 2}

        sorted_tasks = sorted(
            project_tasks,
            key=lambda t: priority_order.get(t["priority"].lower(), 999)
        )

        print(f"Taken in '{project}' (gesorteerd hoog → laag):\n")

        for t in sorted_tasks:
            icon = "✓" if t["status"] == "afgerond" else " "
            prio = t["priority"].upper()
            print(f"[{icon}] {t['id']:3d}: {t['title']}  ({prio})")
            print(f"    {t['description']}")
            print(f"    Status: {t['status']} | Aangemaakt: {t['created_at'][:10]}\n")

    def mark_done(self, task_id):
        for t in self.tasks:
            if t["id"] == task_id:
                t["status"] = "afgerond"
                self.save()
                print(f"Taak {task_id} afgerond")
                return
        print(f"Taak ID {task_id} niet gevonden")

    def remove_task(self, task_id):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) == before:
            print(f"Taak ID {task_id} niet gevonden")
            return
        self.save()
        print(f"Taak {task_id} verwijderd")

    # NIEUW: zoekfunctie op titel
    def search(self, zoekterm):
        zoekterm = zoekterm.lower().strip()
        if not zoekterm:
            print("Geef een zoekterm op")
            return

        matches = [t for t in self.tasks if zoekterm in t["title"].lower()]

        if not matches:
            print(f"Geen taken gevonden met '{zoekterm}' in de titel")
            return

        print(f"Zoekresultaten voor '{zoekterm}' ({len(matches)} gevonden):\n")

        priority_order = {"hoog": 0, "medium": 1, "laag": 2}
        sorted_matches = sorted(
            matches,
            key=lambda t: priority_order.get(t["priority"].lower(), 999)
        )

        for t in sorted_matches:
            icon = "✓" if t["status"] == "afgerond" else " "
            prio = t["priority"].upper()
            short_desc = t["description"][:60] + "..." if len(t["description"]) > 60 else t["description"]
            print(f"[{icon}] {t['id']:3d} | {t['project']:<15} | {t['title']} ({prio})")
            print(f"    {short_desc}")
            print(f"    Status: {t['status']} | Aangemaakt: {t['created_at'][:10]}\n")