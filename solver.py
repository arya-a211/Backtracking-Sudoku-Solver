def print_board(table):
    rows, cols = 9, 9
    mn = ""
    for i in range(rows):
        for j in range(cols):
            if j % 3 == 0:
                mn += f" | {str(table[i][j])}"
            else:
                mn += f" {str(table[i][j])}"
        if j == cols - 1:
            mn += " |"
        if i % 3 == 0:
            print("  ------------------------ ")
        print(mn)
        if i == rows - 1:
            print("  ------------------------ ")
        mn = ""


def check_validity(table, position):
    # checking if row is valid
    number = table[position[0]][position[1]]
    for j in range(9):
        if j != position[1] and number == table[position[0]][j]:
            return False
    # checking if col is valid
    for i in range(9):
        if i != position[0] and number == table[i][position[1]]:
            return False
    # checking if grid is valid
    start_row, start_col = position[0] // 3 * 3, position[1] // 3 * 3
    for i in range(3):
        for j in range(3):
            if (start_row + i != position[0] or start_col + j != position[1]) and number == table[start_row + i][
                start_col + j]:
                return False
    # if all the above were valid, return True
    return True


# this method is for testing an entire Sudoku board to see if it's solved or not
def check_board_valid_and_full(table):
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0 or not check_validity(table, (i, j)):
                return False
    return True


def sudoku_solver_backtracking(table):
    # if the Sudoku is solved, return
    if check_board_valid_and_full(table):
        print("solution: ")
        print_board(table)
        return True
    for i in range(9):
        for j in range(9):
            # we use 0 for showing empty spaces
            if table[i][j] == 0:
                # trying to put numbers until one of them is valid..
                for number in range(9):
                    table[i][j] = number + 1
                    if check_validity(table, (i, j)):
                        # if we placed a valid number, recursive call on current state of table
                        if sudoku_solver_backtracking(table):
                            return True
                # we failed putting [1 to 9] in the cell, backtrack to the modified cell before it
                table[i][j] = 0
                return False
    print("Sudoku not valid. no solution exists =(")

#default puzzle to solve
ar = [[4, 0, 0, 3, 0, 7, 0, 0, 6],
      [0, 3, 0, 4, 0, 5, 0, 0, 0],
      [0, 0, 0, 9, 0, 0, 0, 4, 0],
      [2, 8, 0, 0, 0, 0, 4, 0, 0],
      [0, 0, 5, 0, 0, 0, 0, 6, 0],
      [3, 4, 9, 0, 0, 0, 7, 0, 0],
      [9, 7, 0, 8, 2, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 7, 4],
      [6, 2, 0, 0, 0, 0, 9, 8, 0]]

sudoku_solver_backtracking(ar)
