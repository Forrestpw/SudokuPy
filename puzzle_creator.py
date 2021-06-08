from random import sample
import solver


# Create a solved sudoku of size 9 x 9
def create_board():
    board = []
    # Creates an empty list for rows[0] and a random list for rows[1]
    rows = [[], sample(range(1, 10), 9)]
    j = 0

    # Creates a random row that doesn't contradict the other row in rows
    for i in rows[1]:
        j = i + 2

        if j > 9:
            j = j - 9

        rows[0].append(j)

    # fills the board with lists
    # the first list(board[0]) being randomized and board[1] - board[8] being filled with 0s
    for i in range(9):
        if i == 0:
            board.append(rows[0])
            continue
        if i == 3:
            board.append(rows[1])
            continue

        board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    # Solves the board giving a correct sudoku puzzle
    solver.solve(board)

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
        zero_board.append(sample([0] * num_zeros + [1] * (9 - num_zeros), 9))

    return zero_board


# fills the given solved sudoku with zeros
# and symmetrically mirrors the zeros on the board as if the puzzle was folded in half diagonally
def add_zeros_to_board(bo, difficulty):
    midpoint = len(bo) // 2
    end_row = len(bo) - 1
    end_col = len(bo[0]) - 1
    zero_board = create_zero_board(difficulty)

    # iterates through the zero_board looking for zeros
    # when a zero is found replace the value of the same location on the sudoku board with a zero
    # then mirror it to the other portion of the board for a symmetrical puzzle
    for i in range(len(zero_board)):
        for j in range(len(bo[0])):

            if i == midpoint and j > midpoint:
                break

            if zero_board[i][j] == 0:
                bo[i][j] = 0
                bo[end_row][end_col] = 0

            end_col -= 1
        end_col = len(bo[0]) - 1
        end_row -= 1

    return bo
