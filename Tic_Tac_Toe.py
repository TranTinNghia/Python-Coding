# Print the "Tic-Tac_Toe" board:
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}   ",end="")
        print("\n")

# Quit the program:
def quit_program(user_input):
    if (user_input.lower() == "q") or (user_input.lower() == "quit"):
        print(">>> Thanks for playing!")
        return True
    else: return False

# Check if the user input is valid or not (Must be an integer and in the range of 1 to 9):
def check_user_input_validity(user_input):
    if not user_input.isnumeric():
        print(">>> The input is not valid. Please type again!")
        return False
    else: return check_range_user_input(user_input)

# Check if the user input is in the range of 1 to 9 or not:
def check_range_user_input(user_input):
    if (int(user_input) >= 1) and (int(user_input) <= 9): return True
    else:
        print(">>> The input is out the bound. Please type a number between 1 and 9!")
        return False

# The position of user input:
def coordinate(user_input):
    rows = int(user_input / 3)
    columns = user_input
    if int(user_input) > 2:
        columns = int(columns % 3)
    else: pass
    return (rows,columns)

# Check if the slot has been taken or not:
def taken_or_not(coordinates, board):
    row = coordinates[0]
    column = coordinates[1]
    if board[row][column] != "-":
        print(">>> This position has already been taken!")
        return True
    else: return False

# Add "X" or "O" to the slot:
def add_to_board(coordinates, board, active_user):
    row = coordinates[0]
    column = coordinates[1]
    board[row][column] = active_user

def current_user(user):
    if user == True: return "X"
    else: return "O"

# Check result:
def win_lose(user, board):
    if check_row(user, board): return True
    else: pass
    if check_column(user, board): return True
    else: pass
    if check_diagonal(user, board): return True
    else: pass
    return False

# Check in row:
def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
            else: pass
        if complete_row: return True
        else: pass
    return False

# Check in column:
def check_column(user, board):
    for column in range(3):
        complete_column = True
        for row in range(3):
            if board[row][column] != user:
                complete_column = False
                break
            else: pass
        if complete_column: return True
        else: pass
    return False

# Check in diagonal:
def check_diagonal(user, board):
    if (board[0][0] == user) and (board[1][1] == user) and (board[2][2] == user): return True
    elif (board[0][2] == user) and (board[1][1] == user) and (board[2][0] == user): return True
    else: return False

if __name__ == "__main__":
    board = [["-" for r in range(3)] for c in range(3)] # r for row and c for column.
    user = True # True refers to "X", otherwise "O".
    turn = 0
    while turn < 9: # Turn must be less than 9 so that win and lose occur. If Turn = 9, it is a tie.
        active_user = current_user(user)
        print_board(board)
        user_input = input("Please type a number from 1 through 9 or press \"q\" to quit!: ")
        if quit_program(user_input): break
        elif not check_user_input_validity(user_input): continue
        else:
            user_input = int(user_input) - 1
            coordinates = coordinate(user_input)
            if taken_or_not(coordinates, board): continue
            else:
                add_to_board(coordinates, board, active_user)
        if win_lose_tie(active_user,board):
            print_board(board)
            print(f">>> {active_user.upper()} won! <<< \n")
            break
        else: pass
        turn = turn + 1
        # Tie occurs:
        if turn == 9:
            print_board(board)
            print(">>> Both tied! <<< \n")
        else: pass
        # Switch between "X" and "O":
        user = not user
