# Sudoko Solver Program

## Description

- This Python program solves Sudoku puzzles automatically using the backtracking algorithm.
- It takes an input grid representing an unsolved Sudoku puzzle and fills in the missing numbers to find the correct arrangement of numbers for the puzzle. 
- Once solved, the program displays the completed Sudoku grid.

## Steps For Creating a Sudoko Solver Program

- Input Parsing: Parse the input grid representing the unsolved Sudoku puzzle.
- Check Validity: Check if the input grid is a valid Sudoku grid.
- Backtracking Algorithm: Implement a backtracking algorithm to solve the Sudoku puzzle recursively.
- Check Constraints: At each step of the backtracking algorithm, check if the current grid configuration satisfies the Sudoku constraints (no repeated numbers in rows, columns, or 3x3 subgrids).
- Backtrack and Retry: If the current configuration violates the constraints, backtrack to the previous step and try a different number.
- Base Case: Stop the recursion when the puzzle is solved completely (all cells are filled).
- Output: Once the puzzle is solved, display the completed Sudoku grid.


## How to Use

1. Make sure you have Python installed on your system.
2. Download or clone the repository to your local machine.
3. Open a terminal or command prompt and navigate to the directory where the program is located.
4. Run the program by executing the following command:
 
    python Sudoko_Solver.py
5. **Enter the Sudoku Puzzle**: Follow the instructions to enter the Sudoku puzzle. Use `0` to represent empty cells.

5. **View the Solution**
## Features

- Automatic solving of Sudoku puzzles
- Input grid validation
- Backtracking algorithm for finding solutions
- Simple command-line interface
