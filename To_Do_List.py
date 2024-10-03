def display_menu():
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_tasks(tasks):
    try:
        n_tasks = int(input("\nHow many tasks do you want to add: "))
        for _ in range(n_tasks):
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
            print("Task added!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")

def mark_task_done(tasks):
    try:
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_tasks(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()