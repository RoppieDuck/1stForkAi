import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Project & Task Manager CLI")
    sub = parser.add_subparsers(dest="command")

    add_project = sub.add_parser("add_project")
    add_project.add_argument("name")

    add_task = sub.add_parser("add_task")
    add_task.add_argument("project")
    add_task.add_argument("title")

    list_cmd = sub.add_parser("list")
    list_cmd.add_argument("project")

    return parser.parse_args()