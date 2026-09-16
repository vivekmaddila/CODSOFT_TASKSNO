# CODSOFT Python Programming Internship
# Task 1 - To-Do List Application

tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n----- YOUR TASKS -----")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a new task: ").strip()

    if task:
        tasks.append(task)
        print("✅ Task added successfully!")
    else:
        print("❌ Task cannot be empty.")


def update_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to update: "))

        if 1 <= number <= len(tasks):
            new_task = input("Enter the updated task: ").strip()

            if new_task:
                tasks[number - 1] = new_task
                print("✅ Task updated successfully!")
            else:
                print("❌ Task cannot be empty.")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print(f"✅ Deleted: {deleted_task}")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    while True:
        print("\n==============================")
        print("       TO-DO LIST APP")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("\nThank you for using To-Do List App! 👋")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()