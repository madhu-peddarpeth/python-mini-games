def play():
    print("\n🎮 TIC-TAC-TOE")

    board = [" "] * 9
    player = "X"

    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    while True:
        print()
        for i in range(0, 9, 3):
            print(" | ".join(board[i:i + 3]))
            if i < 6:
                print("--+---+--")

        try:
            position = int(
                input(f"Player {player}, choose (1-9): ")
            ) - 1
        except ValueError:
            print("Please enter a number.")
            continue

        if position not in range(9):
            print("Choose a position from 1 to 9.")
            continue

        if board[position] != " ":
            print("Position already taken!")
            continue

        board[position] = player

        if any(
            board[a] == board[b] == board[c] == player
            for a, b, c in wins
        ):
            for i in range(0, 9, 3):
                print(" | ".join(board[i:i + 3]))
            print(f"Player {player} wins! 🎉")
            break

        if " " not in board:
            for i in range(0, 9, 3):
                print(" | ".join(board[i:i + 3]))
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"