import random

while True:
    choice = input("Do you want to roll again? (y/n): ")

    if choice == "y" or "Y":
        random_dice_roll = random.randint(1, 6)
        print("Rolling...")
        print(f"Dice Rolled: {random_dice_roll}")
        continue
    else:
        break
