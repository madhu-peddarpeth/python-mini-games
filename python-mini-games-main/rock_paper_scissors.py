import random

def play():
    print("\n🎮 ROCK PAPER SCISSORS")

    choices = ["rock", "paper", "scissors"]

    while True:
        user = input(
            "Choose rock, paper, scissors (or quit): "
        ).lower().strip()

        if user == "quit":
            print("Returning to main menu...")
            break

        if user not in choices:
            print("Invalid choice. Try again.")
            continue

        computer = random.choice(choices)
        print("Computer chose:", computer)

        if user == computer:
            print("It's a tie!")
        elif (
            (user == "rock" and computer == "scissors")
            or (user == "paper" and computer == "rock")
            or (user == "scissors" and computer == "paper")
        ):
            print("You win! 🎉")
        else:
            print("Computer wins!")