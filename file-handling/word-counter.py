
def count_words(file_path):
    with open(file_path, 'r') as file:
        return len(file.read().split())

file = "text.txt"

words = count_words(file)

print(f"Total words in file: {words}")
