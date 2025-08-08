tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Added task: {task}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "3":
        if not tasks:
            print("Nothing to remove.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "4":
        print("Goodbye! Your productivity just got a boost. 💪")
        break

    else:
        print("Invalid choice. Please enter 1-4.")