# Simple Connect Four (2 players) - Console Version

ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n " + " ".join(str(i) for i in range(COLS)))
    for row in board:
        print("|" + "|".join(row) + "|")
    print("-" * (COLS * 2 + 1))

def drop_piece(board, col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            return True
    return False  # if column is full

def winning_move(board, piece):
    # Horizontal check
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    # Vertical check
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    # Diagonal (positive slope)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    # Diagonal (negative slope)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def is_board_full(board):
    return all(board[0][c] != " " for c in range(COLS))

def play_game():
    board = create_board()
    turn = 0  # Player 1 starts
    pieces = ["X", "O"]
    print("Welcome to Connect Four!")
    print("Player 1 = X | Player 2 = O")
    print_board(board)

    while True:
        player = turn % 2
        piece = pieces[player]
        print(f"\nPlayer {player + 1}'s turn ({piece})")

        try:
            col = int(input(f"Choose a column (0-{COLS - 1}): "))
            if not (0 <= col < COLS):
                print("Invalid column number. Try again.")
                continue
            if not drop_piece(board, col, piece):
                print("That column is full! Choose another.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        print_board(board)

        if winning_move(board, piece):
            print(f"\n🎉 Player {player + 1} ({piece}) wins! 🎉")
            break

        if is_board_full(board):
            print("\nIt's a draw! Board is full.")
            break

        turn += 1

if __name__ == "__main__":
    play_game()
