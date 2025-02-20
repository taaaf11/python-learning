import random

print("=== A number guessing game ===")

max_range = int(input("Enter the range: "))

random_number = random.randint(1, max_range)

while True:
    guess = int(input("Guess a number: "))

    if guess == random_number:
        print(f"Congratulations! You guessed the number {guess}!")
    elif guess > random_number:
        print(f"Sorry, the number {guess} is too high!")
    else:
        print(f"Sorry, the number {guess} is too low!")
