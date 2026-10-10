import random

def play():
    print("\n🎯 NUMBER GUESSING GAME")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
            elif guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You won in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
