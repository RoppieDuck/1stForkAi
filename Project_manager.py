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
        except:
            return []

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.projects, f, indent=4)

    def add_project(self, name):
        if not name.strip():
            print("Projectnaam mag niet leeg zijn")
            return

        if any(p["name"].lower() == name.lower() for p in self.projects):
            print(f"Project '{name}' bestaat al")
            return

        project = Project(name=name).__dict__
        self.projects.append(project)
        self.save()
        print(f"Project '{name}' toegevoegd")

    def list_projects(self):
        from Task_manager import TaskManager
        task_manager = TaskManager()

        if not self.projects:
            print("Er zijn nog geen projecten")
            return

        print("Overzicht van alle projecten:\n")

        for p in self.projects:
            project_name = p["name"]

            project_tasks = [
                t for t in task_manager.tasks
                if t["project"].lower() == project_name.lower()
            ]

            total = len(project_tasks)
            done = len([t for t in project_tasks if t["status"] == "afgerond"])
            open_tasks = total - done

            if total == 0:
                status = "Geen taken"
            elif done == total:
                status = "Voltooid"
            else:
                status = "In uitvoering"

            print(f"- {project_name}")
            print(f"  Status: {status}")
            print(f"  Taken totaal: {total}")
            print(f"  Open: {open_tasks}, Afgerond: {done}\n")

    # NIEUW: project_stats methode
    def project_stats(self, project_name):
        from Task_manager import TaskManager
        task_manager = TaskManager()

        if not any(p["name"].lower() == project_name.lower() for p in self.projects):
            print(f"Project '{project_name}' bestaat niet")
            return

        project_tasks = [
            t for t in task_manager.tasks
            if t["project"].lower() == project_name.lower()
        ]

        total = len(project_tasks)
        if total == 0:
            print(f"\n{project_name}")
            print("  → Geen taken\n")
            return

        counts = {"open": 0, "bezig": 0, "afgerond": 0}

        for t in project_tasks:
            s = t["status"].lower()
            counts[s if s in counts else "open"] += 1

        done = counts["afgerond"]
        perc = (done / total * 100) if total else 0

        print(f"\nStatistieken: {project_name}")
        print(f"  Totaal:      {total}")
        print(f"  Open:        {counts['open']}")
        print(f"  Bezig:       {counts['bezig']}")
        print(f"  Afgerond:    {done}")
        print(f"  Afgerond %:  {perc:.1f}%")
        print()