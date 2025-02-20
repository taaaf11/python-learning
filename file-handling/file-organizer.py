
import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory not found.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isdir(file_path):
            continue

        file_extension = file.split('.')[-1] if '.' in file else "Other"
        folder_path = os.path.join(directory, file_extension.upper())

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(file_path, os.path.join(folder_path, file))

    print("Files organized successfully.")

organize_files(os.getcwd())