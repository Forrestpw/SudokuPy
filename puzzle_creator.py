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
