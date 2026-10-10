def main():
    while True:
        print("\n PYTHON MINI GAMES")
        print("1. Number Guessing")
        print("2. Rock Paper Scissors")
        print("3. Tic-Tac-Toe")
        print("4. Exit")

        choice = input("Choose a game (1-4): ")

        if choice == "1":
            import number_guessing
            number_guessing.play()
        elif choice == "2":
            import rock_paper_scissors
            rock_paper_scissors.play()
        elif choice == "3":
            import tic_tac_toe
            tic_tac_toe.play()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()