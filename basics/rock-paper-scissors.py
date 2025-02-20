import random

while True:
    print("(Rock, Paper, Scissors) Game")

    game_modes = ["Rock", "Paper", "Scissors"]
    computer_pick = random.choice(game_modes)

    print("1. Rock\n2. Paper\n3. Scissors")
    user_pick = input("Enter your choice: ")

    print("Computer pick: ", computer_pick)

    game_won_by = ""

    if user_pick == "Rock" and computer_pick == "Scissors":
        game_won_by += "User"
        print(f"{game_won_by} won the game!")
    elif user_pick == "Paper" and computer_pick == "Scissors":
        game_won_by += "Computer"
        print(f"{game_won_by} won the game!")
    elif user_pick == "Scissors" and computer_pick == "Rock":
        game_won_by += "Computer"
        print(f"{game_won_by} won the game!")
    elif user_pick == "Rock" and computer_pick == "Paper":
        game_won_by += "Computer"
        print(f"{game_won_by} won the game!")
    elif user_pick == computer_pick:
        print("It's a tie!")
    else:
        print("Please enter a valid choice.")