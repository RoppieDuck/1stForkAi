import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Project & Task Manager CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # -----------------------------
    # PROJECT COMMANDS
    # -----------------------------

    # Project toevoegen
    add_project = sub.add_parser(
        "add_project",
        help="Voeg een nieuw project toe"
    )
    add_project.add_argument("name", help="Naam van het project")

    # Alle projecten tonen
    sub.add_parser(
        "list_projects",
        help="Toon alle projecten met status en aantal taken"
    )

    # -----------------------------
    # TASK COMMANDS
    # -----------------------------

    # Taak toevoegen
    add_task = sub.add_parser(
        "add_task",
        help="Voeg een taak toe aan een project"
    )
    add_task.add_argument("project", help="Naam van het project")
    add_task.add_argument("title", help="Titel van de taak")
    add_task.add_argument("description", help="Beschrijving van de taak")
    add_task.add_argument(
        "priority",
        help="Prioriteit van de taak (laag, medium, hoog)"
    )

    # Taken tonen
    list_tasks = sub.add_parser(
        "list_tasks",
        help="Toon alle taken van een project"
    )
    list_tasks.add_argument("project", help="Naam van het project")

    # Taak afronden
    done = sub.add_parser(
        "done",
        help="Markeer een taak als afgerond"
    )
    done.add_argument("id", type=int, help="ID van de taak")

    # Taak verwijderen
    remove = sub.add_parser(
        "remove_task",
        help="Verwijder een taak op basis van ID"
    )
    remove.add_argument("id", type=int, help="ID van de taak")

    return parser.parse_args()