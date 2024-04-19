def is_valid(board, row, col, num):
    # Check if num is not already in current row, column, or 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[row//3*3 + i//3][col//3*3 + i%3] == num:
            return False
    return True

def solve_sudoku(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing numbers 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def get_input_grid():
    print("Enter the Sudoku puzzle (use 0 for empty cells):")
    grid = []
    for i in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

input_grid = get_input_grid()

if solve_sudoku(input_grid):
    print("Sudoku puzzle solved:")
    print_board(input_grid)
else:
    print("No solution exists.")