# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array
# representing a Sudoku board, and returns true if it is a valid solution, or false otherwise.
# The cells of the sudoku board may also contain 0's, which will represent empty cells.
# Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

x_true = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 9]]

x_false = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
           [6, 7, 2, 1, 9, 5, 3, 4, 8],
           [1, 9, 8, 3, 4, 2, 0, 6, 7],
           [8, 5, 9, 7, 6, 1, 4, 2, 3],
           [4, 2, 6, 8, 5, 3, 7, 9, 1],
           [7, 1, 3, 9, 2, 4, 8, 5, 6],
           [9, 6, 1, 5, 3, 7, 2, 8, 4],
           [2, 8, 7, 4, 1, 9, 6, 3, 5],
           [3, 4, 5, 2, 8, 6, 1, 7, 9]]


def valid_solution(board):
    allowed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in board:
        if sorted(row) != allowed_numbers:
            return False

    for idx, row in enumerate(board):
        col_check = []
        block_check = []
        for i in range(0, 9):
            col_check.append(board[i][idx])
            if (idx+3) % 3 == 0:
                block_check.append(board[i][idx:idx+3])

        if block_check:
            square = []
            for x, item in enumerate(block_check):
                if (x+3) % 3 == 0:
                    for items in range(0, 3):
                        square = square + block_check[x+items]

            for x in range(0, 27, 9):

                if sorted(square[x:x+9]) != allowed_numbers:
                    return False

        if sorted(col_check) != allowed_numbers:
            return False

    return True


print(valid_solution(x_true))
