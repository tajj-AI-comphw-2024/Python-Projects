# To-Do List Manager
# Skills Used: Lists, dictionaries, loops, and functions.
# Build a program where users can add, delete, or view tasks in a to-do list.
# Enhance it by categorizing tasks (e.g., "work," "personal") using dictionaries.
# Goal: Practice CRUD (Create, Read, Update, Delete) operations with Python data structures.

def create_task(task_name, category):
    tasks = load_tasks()
    tasks[task_name] = category
    save_tasks(tasks)
    print(f"Task '{task_name}' added to category '{category}'.")

def delete_task(task_name):
    tasks = load_tasks()
    if task_name in tasks:
        del tasks[task_name]
        save_tasks(tasks)
        print(f"Task '{task_name}' deleted.")
    else:
        print(f"Task '{task_name}' not found.")

def view_tasks(category):
    tasks = load_tasks()
    print(f"Tasks in category '{category}':")
    for task, task_category in tasks.items():
        if task_category == category:
            print(task)

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = eval(file.read())
        return tasks
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error loading tasks: {str(e)}")
        return {}

def save_tasks(tasks):
    try:
        with open("tasks.txt", "w") as file:
            file.write(str(tasks))
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {str(e)}")

def main():
    print("Welcome to the To-Do List Manager!")
    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View tasks by category")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task_name = input("Enter the task name: ")
            category = input("Enter the category (work, personal): ")
            create_task(task_name, category)
        elif choice == "2":
            task_name = input("Enter the task name to delete: ")
            delete_task(task_name)
        elif choice == "3":
            category = input("Enter the category to view: ")
            view_tasks(category)
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
