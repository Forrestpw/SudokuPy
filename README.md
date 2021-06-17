# About
SudokuPy first started out as a script that used a back tracking algorithm to solve any Sudoku puzzle. Now, the project has come further and is able to use the back tracking algorthim to generate a valid Sudoku puzzle to be solved, that paired with pygame created a nice little Sudoku game for the desktop.

## How it works

[solver.py](https://github.com/forrestpatwalker/SudokuPy/blob/main/solver.py) this is where the back tracking algorithm lies. How it works is it will plug in a valid number for the current Sudoku square and move forward until it no longer has any valid numbers it can plug in to the square it gets to. It will then move back and try swapping its current number with that of the last square it was in, if that still results in an invalid number for that square it will again move back another square and will continue to repeat this process until it generates a valid solution for the whole board. If it as a valid Sudoku puzzle this will solve the board.

[puzzle_creator.py](https://github.com/forrestpatwalker/SudokuPy/blob/main/puzzle_creator.py) is where the board is generated for the game. The process is to generate two random rows that would be valid for a sudoku and then allowing [solver.py](https://github.com/forrestpatwalker/SudokuPy/blob/main/solver.py) to solve the rest of the board, therefore creating a random valid Sudoku board. Using half the demensions of the that board another board is generated with just 0's and 1's, 0's representing what squares of the sudoku that will be hidden from the player based on a difficulty setting. The reason we only generate a board of half the size is because Sudoku boards are generally symmetrical. The function `def add_zeros_to_board` takes the zero's from the zero_board replaces the squares in the already solved board with those 0's (0's are used to represent blank spaces on the board) every space that is filled with a 0 will also fill its symmetrical counterpart with a 0 as well.

Now that we have a valid board that is symmetrical and filled with 0's (based on the players difficulty level) we use this board to generate a GUI with pygame, you will find that code in the [GUI.py](https://github.com/forrestpatwalker/SudokuPy/blob/main/GUI.py) file. In the end the gui looks like this: ![Screenshot from 2021-06-08 13-20-28](https://user-images.githubusercontent.com/17036585/121244644-585d7b80-c85c-11eb-9023-f60ff18b0430.png)
 

As you will see the board is symmetrical, the current selected square is highlighted by a red box, inside the box you can see my current entry I can submit it by pressing enter, a red X indicates the number of failed attempts in the bottom left, and a timer in the bottom right.


## Setup
You will need python installed on your machine (you can get that from [here](https://www.python.org/)) and an IDE of your choice I use [PyCharm](https://www.jetbrains.com/pycharm/)
1. Set up your virtual enviornment, [here](https://realpython.com/python-virtual-environments-a-primer/) is a great guide on this from the guys at Real Python
1. run the following pip installs in your virual enviornment:
  * ``` pip install pygame ```
3. Now just run the GUI.py file and it should open up the game for you to play.
