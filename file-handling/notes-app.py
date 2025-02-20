notes_file = "notes.txt"

def add_note(note_id, note_name, note_status):
    with open(notes_file, 'a') as file:
        file.write(f"Note ID: {note_id}\n")
        file.write(f"Note Name: {note_name}\n")
        file.write(f"Note Status: {note_status}\n")
        file.write("\n")

def view_notes():
    with open(notes_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())

def delete_note(note_id):
    with open(notes_file, 'r') as file:
        lines = file.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Note ID:") and note_id in lines[i]:
            i += 4
        else:
            new_lines.append(lines[i])
            i += 1

    with open(notes_file, 'w') as file:
        file.writelines(new_lines)

while True:
    print("=== Notes App ===")
    print("1. Add Note\n2. View Notes\n3. Delete Note\n4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note_id = input("Enter note ID: ")
        note_name = input("Enter note name: ")
        note_status = input("Enter note status: ")
        add_note(note_id, note_name, note_status)
    elif choice == "2":
        print("\nNotes:\n")
        view_notes()
        print("\n")
    elif choice == "3":
        note_id = input("Enter note ID to delete: ")
        delete_note(note_id)
    elif choice == "4":
        break
    else:
        print("Please enter a valid choice")
