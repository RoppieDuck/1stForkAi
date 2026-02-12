from Project_manager import ProjectManager
from Task_manager import TaskManager
from Utils import parse_arguments

def main():
    args = parse_arguments()
    project_manager = ProjectManager()
    task_manager = TaskManager()

    if args.command == "add_project":
        project_manager.add_project(args.name)

    elif args.command == "add_task":
        task_manager.add_task(args.project, args.title)

    elif args.command == "list":
        task_manager.list_tasks(args.project)

if __name__ == "__main__":
    main()