todo_list = []

def show_menu():
    print("\nTo-Do List")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nTasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")

    elif choice == '2':
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added.")

    elif choice == '3':
        if not todo_list:
            print("No tasks to delete.")
        else:
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(todo_list):
                    deleted = todo_list.pop(task_num - 1)
                    print(f"Deleted task: {deleted}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")