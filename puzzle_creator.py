from random import sample
import solution


# Create a solved sudoku of size 9 x 9
def create_board():
    board = []

    # fills the board with lists
    # the first list(board[0]) being randomized and board[1] - board[8] being filled with 0s
    for i in range(9):
        if i == 0:
            board.append(sample(range(1, 10), 9))
        else:
            board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    # Solves the board giving a correct sudoku puzzle
    solution.solve(board)

    return board


# creates a board of 0s and 1s of size 5 x 9
# number of 0s is based on the given difficulty level
def create_zero_board(difficulty):
    if str.lower(difficulty) == "medium":
        num_zeros = 5
    elif str.lower(difficulty) == "hard":
        num_zeros = 6
    else:
        num_zeros = 4

    zero_board = []

    # Fills each row with 0s and 1s randomly
    # Each row has an exact number of 0s based on difficulty setting
    for i in range(5):
        zero_board.append(sample([0]*num_zeros + [1]*(9-num_zeros), 9))

    return zero_board
