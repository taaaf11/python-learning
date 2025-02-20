TODO_FILE = "todos.txt"

def add_task(task):
    with open(TODO_FILE, 'a') as file:
        file.write(task + "\n")

def delete_task(task):
    with open(TODO_FILE, 'r') as file:
        lines = file.readlines()

    with open(TODO_FILE, 'w') as file:
        for line in lines:
            if task.strip() not in line.strip():
                file.write(line)

def show_tasks():
    with open(TODO_FILE, 'r') as file:
        lines = file.readlines()

    for id, line in enumerate(lines, 1):
        print(f"{id}: {line.strip()}")

print("Tasks added: ")

add_task("Task 1 is added successfully")
add_task("Task 2 is added successfully")
show_tasks()

print("Tasks after deletion: ")

delete_task("Task 2 is added successfully")
show_tasks()
