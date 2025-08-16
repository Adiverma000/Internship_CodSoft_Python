def show_menu():
    print("\n----Menu----:")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{index}. {task['name']} - {status}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({'name': title, 'completed': False})
        print(f"Task '{title}' added successfully.")
    else:
        print("Task title cannot be empty.")

def mark_task_completed(tasks):
    if not tasks:
        print("No tasks to mark. Add a task first.")
        return
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            print(f"Task '{tasks[task_index]['name']}'completed Good job!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete. Add a task first.")
        return
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed = tasks.pop(task_index)
            print(f"Task '{removed['name']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
# Program execution starts here
tasks = []

print("Welcome to your to-do list application!")
while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()
    if choice == '1':
        view_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        mark_task_completed(tasks)
    elif choice == '4':
        delete_task(tasks)
    elif choice == '5':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
