tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\nOptions: add | remove | view | exit")
    action = input("Choose an action: ").lower()

    if action == "add":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif action == "remove":
        show_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            tasks.pop(task_num - 1)
            print("Task removed.")
        except:
            print("Invalid input.")
    elif action == "view":
        show_tasks()
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please try again.")
