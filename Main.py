from Project_manager import ProjectManager
from Task_manager import TaskManager
from Utils import parse_arguments

def main():
    args = parse_arguments()

    project_manager = ProjectManager()
    task_manager = TaskManager()

    if args.command == "add_project":
        project_manager.add_project(args.name)

    elif args.command == "list_projects":
        project_manager.list_projects()

    elif args.command == "project_stats":
        project_manager.project_stats(args.project)

    elif args.command == "add_task":
        task_manager.add_task(
            args.project,
            args.title,
            args.description,
            args.priority
        )

    elif args.command == "list_tasks":
        task_manager.list_tasks(args.project)

    elif args.command == "done":
        task_manager.mark_done(args.id)

    elif args.command == "remove_task":
        task_manager.remove_task(args.id)

    elif args.command == "search":
        task_manager.search(args.zoekterm)

if __name__ == "__main__":
    main()