board = [
    [0,0,7,0,4,0,5,8,2],
    [5,0,2,0,0,8,6,4,0],
    [6,8,4,0,5,0,7,3,0],
    [0,6,0,0,0,0,4,0,0],
    [4,0,3,0,0,6,0,5,8],
    [9,2,0,3,8,0,1,7,0],
    [2,0,6,0,9,3,8,0,7],
    [8,4,0,0,1,0,3,0,5],
    [7,0,0,8,6,5,2,0,0]
]

class SudokuSolver():
    def find(self, board):
        for i in range(0,9):  # scan down
            for j in range(0,9):  # scan right
                if board[i][j] == 0:
                    pos = i, j
                    return i, j
        return None


    def valid(self, bo, number, g, h):
        row, col = g, h
        for i in range(9):  # checking rows here
            if bo[row][i] == number and i != col:
                return False

        for j in range(9):  # checking columns here
            if bo[j][col] == number and j != row:
                return False

        box_x = col // 3
        box_y = row // 3

        for a in range(box_y*3, box_y*3+3):
            for b in range(box_x*3, box_x*3+3):
                if bo[a][b] == number and g != a and h != b:
                    return False

        return True


    def solve(self, bo):
        empty_space = self.find(bo)

        if not empty_space:
            return True
        else:
            row, col = empty_space
            for i in range(1, 10):
                if self.valid(bo, i, empty_space[0], empty_space[1]):
                    bo[row][col] = i
                    print(bo)

                    if self.solve(bo):
                        return True

                    bo[row][col] = 0
