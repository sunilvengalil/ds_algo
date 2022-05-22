# def verify_solution(board):
#     for each row:
#
#
# def get_feasible_digits():
#     row = cell[0]
#     col = cell[1]
#     for i in range(9):
#
#         if i is present in the row
#         continue
#     if i is present in the col
#     cotinue
#
#
# def get_next_empty_cell(board, row, col):
#     # return the next empty cell in the board after (row, col)
#     while row < 9 and col < 9 and board[row][col] != ".":
#         if col < 9:
#             if row < 9:
#                 row = row + 1
#             else:
#                 col += 1
#                 row = 0
#         else:
#             # last col
#             row += 1
#     if row < 9 and col < 9:
#         return row, col
#     else:
#         return -1, -1
#
#
# def sudoku_solve(board):
#     empty_cell = get_empty_cell(0, 0)
#     while empty_cell[0] != -1 and empty_cell[1] != -1:
#         stack = [empty_cell, digit]
#         result = False
#         while stack is not empty:  # O()
#             cell = stack.pop()
#             feasible_digits_list = get_feasible_digits(board, cell)  # O(n^2)
#             if verify_solution(board):  # O(n^2)
#                 result = True
#                 break
#             for digit in feasible_cells:
#                 stack.push([cell, digit])
#
#         return True
#
#     # for each non-empty cell from top to bottom and left to right:
#
#     pass  # your code goes here
#
#
#
#
#

def valid_row(row):
    # check each row
    val_present = [False] * 9
    for c in range(9):
        if row[c] != ".":
            if val_present[int(row[c]) - 1]:
                return False
            val_present[int(row[c]) - 1] = True
    return True

def valid(board):
    for r in range(9):
        if not valid_row(board[r]):
            return False
    for c in range(9):
        row = [board[r][c] for r in range(9)]
        if not valid_row(row):
            return False

    for r in range(3):
        for c in range(3):
            row = [None] * 9
            index = 0
            for i in range(r * 3, (r + 1) * 3):
                for j in range(c * 3, (c + 1) * 3):
                    row[index] = board[i][j]
                    index += 1
            if not valid_row(row):
                return False
    return True


def get_feasible_digits(board, r, c):
    digits = []
    for ch in range(1, 10):
        is_ch_present = False
        for i in range(9):
            if board[r][i] == str(ch) or board[i][c] == str(ch) or board[(r // 3) * 3 + i // 3][
                (c // 3) * 3 + i % 3] == str(ch):
                is_ch_present = True
                break
        if not is_ch_present:
            digits.append(ch)
    return digits

from copy import deepcopy

def sudoku_solve(board):
    if not valid(board):
        return False
    # Get the cell with least number of choices
    minim_choices_cell = [-1, -1]
    lowest_choices = None
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                continue
            possible_digits = get_feasible_digits(board, r, c)
            if lowest_choices is None or len(possible_digits) < len(lowest_choices):
                minim_choices_cell = (r, c)
                lowest_choices = possible_digits
    if lowest_choices is None or len(lowest_choices) == 0:
        return True
#    print("minim_choices_cell", minim_choices_cell)
#    print("choices", lowest_choices)
    new_board = deepcopy(board)
    for ch in lowest_choices:
        new_board[minim_choices_cell[0]][minim_choices_cell[1]] = ch
        if sudoku_solve(new_board):
            return True
    return False

a = [[".",".",".","7",".",".","3",".","1"],
     ["3",".",".","9",".",".",".",".","."],
     [".","4",".","3","1",".","2",".","."],
     [".","6",".","4",".",".","5",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".","1",".",".","8",".","4","."],
     [".",".","6",".","2","1",".","5","."],
     [".",".",".",".",".","9",".",".","8"],
     ["8",".","5",".",".","4",".",".","."]]
b = [[".","8","9",".","4",".","6",".","5"],
     [".","7",".",".",".","8",".","4","1"],
     ["5","6",".","9",".",".",".",".","8"],
     [".",".",".","7",".","5",".","9","."],
     [".","9",".","4",".","1",".","5","."],
     [".","3",".","9",".","6",".","1","."],
     ["8",".",".",".",".",".",".",".","7"],
     [".","2",".","8",".",".",".","6","."],
     [".",".","6",".","7",".",".","8","."]]
print(sudoku_solve(b))