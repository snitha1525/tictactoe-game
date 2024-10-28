def print_board(board):
   
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True, row[0]

 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True, board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True, board[0][2]

    return False, None

def is_board_full(board):
  
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_valid_input(player, board):
 
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] != " ":
                print("That cell is already taken. Try again.")
                continue
            
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
  
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
     
        row, col = get_valid_input(player, board)
        board[row][col] = player
        print_board(board)

        game_over, winner = check_winner(board)
        if game_over:
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

  
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()