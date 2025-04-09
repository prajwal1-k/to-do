# To-Do List App in Python

# A list to store tasks
tasks = []

# Function to display all tasks
def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added to your To-Do list!")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task you want to delete: "))
        if task_num > 0 and task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def complete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task you want to mark as completed: "))
        if task_num > 0 and task_num <= len(tasks):
            completed_task = tasks.pop(task_num - 1)
            print(f"Task '{completed_task}' has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu for the app
def main_menu():
    while True:
        print("\n=== To-Do List App ===")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Delete a task")
        print("4. Mark task as completed")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Exiting the To-Do list app.")
            break
        else:
            print("Invalid choice, please try again.")

# Start the app
if __name__ == "__main__":
    main_menu()