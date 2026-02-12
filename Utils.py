import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Project & Task Manager CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # PROJECT COMMANDS
    add_project = sub.add_parser(
        "add_project",
        help="Voeg een nieuw project toe"
    )
    add_project.add_argument("name", help="Naam van het project")

    sub.add_parser(
        "list_projects",
        help="Toon alle projecten met status en aantal taken"
    )

    project_stats = sub.add_parser(
        "project_stats",
        help="Toon gedetailleerde statistieken van een project"
    )
    project_stats.add_argument("project", help="Naam van het project")

    # TASK COMMANDS
    add_task = sub.add_parser(
        "add_task",
        help="Voeg een taak toe aan een project"
    )
    add_task.add_argument("project", help="Naam van het project")
    add_task.add_argument("title", help="Titel van de taak")
    add_task.add_argument("description", help="Beschrijving van de taak")
    add_task.add_argument(
        "priority",
        choices=["laag", "medium", "hoog"],
        help="Prioriteit: laag | medium | hoog"
    )

    list_tasks = sub.add_parser(
        "list_tasks",
        help="Toon alle taken van een project"
    )
    list_tasks.add_argument("project", help="Naam van het project")

    done = sub.add_parser(
        "done",
        help="Markeer een taak als afgerond"
    )
    done.add_argument("id", type=int, help="ID van de taak")

    remove = sub.add_parser(
        "remove_task",
        help="Verwijder een taak op basis van ID"
    )
    remove.add_argument("id", type=int, help="ID van de taak")

    # NIEUW: zoekfunctie
    search = sub.add_parser(
        "search",
        help="Zoek taken op (deel van) de titel"
    )
    search.add_argument("zoekterm", help="Woord/deel van de taaktitel")

    return parser.parse_args()