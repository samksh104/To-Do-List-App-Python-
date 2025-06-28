import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from a file into a list"""
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks


def save_tasks(tasks):
    """Save tasks from a list into a file"""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    """Display the current list of tasks"""
    if not tasks:
        print("\n✅ No tasks available!\n")
        return
    print("\n📝 To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    """Add a new task"""
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added!\n")
    else:
        print("⚠️  Empty task not added.\n")


def delete_task(tasks):
    """Delete a task by index"""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Removed task: {removed}\n")
        else:
            print("❌ Invalid task number!\n")
    except ValueError:
        print("⚠️  Please enter a valid number.\n")


def mark_done(tasks):
    """Mark a task as completed"""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] += " ✅"
            print(f"🎉 Task marked as done: {tasks[index]}\n")
        else:
            print("❌ Invalid task number!\n")
    except ValueError:
        print("⚠️  Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("🔹 To-Do Menu 🔹")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Save and Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❗ Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
