import numpy as np


def solve_sudoku(sudoku: np.array):
    nrows, ncols = sudoku.shape
    sdim = int(nrows ** 0.5)

    assert nrows == ncols, "sudoku dimensions must be equal."

    def _valid(r, c, n):
        for i in range(nrows):
            if sudoku[r][i] == n:
                return False
        for j in range(ncols):
            if sudoku[j][c] == n:
                return False

        r_, c_ = (r // sdim) * sdim, (c // sdim) * sdim
        for i in range(sdim):
            for j in range(sdim):
                if sudoku[r_ + i][c_ + j] == n:
                    return False
        return True

    def _solve():
        for row in range(ncols):
            for col in range(nrows):
                if sudoku[row][col] == 0:
                    for d in range(1, nrows + 1):
                        if _valid(row, col, d):
                            sudoku[row][col] = d
                            _solve()
                            sudoku[row][col] = 0
                    return
        print(sudoku)
        _check(sudoku)

    def _check(s):
        for row in s:
            d = 0
            for i in range(nrows):
                d = d | (1 << row[i])
            assert (d >> 1) == ((1 << nrows) - 1)

        for col in s.T:
            d = 0
            for i in range(ncols):
                d = d | (1 << col[i])
            assert (d >> 1) == ((1 << ncols) - 1)

        for i in range(sdim):
            r = i * sdim
            for j in range(sdim):
                c, d = sdim, 0
                for k in range(r, r + sdim):
                    for h in range(c, c + sdim):
                        d = d | (1 << s[k][h])
                assert (d >> 1) == ((1 << nrows) - 1)
        return True

    _solve()


if __name__ == '__main__':
    easy = np.array([0, 0, 0, 2, 6, 0, 7, 0, 1,
                     6, 8, 0, 0, 7, 0, 0, 9, 0,
                     1, 9, 0, 0, 0, 4, 5, 0, 0,
                     8, 2, 0, 1, 0, 0, 0, 4, 0,
                     0, 0, 4, 6, 0, 2, 9, 0, 0,
                     0, 5, 0, 0, 0, 3, 0, 2, 8,
                     0, 0, 9, 3, 0, 0, 0, 7, 4,
                     0, 4, 0, 0, 5, 0, 0, 3, 6,
                     7, 0, 3, 0, 1, 8, 0, 5, 0]).reshape(9, 9)

    hard = np.array([0, 2, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 6, 0, 0, 0, 0, 3,
                     0, 7, 4, 0, 8, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 3, 0, 0, 2,
                     0, 8, 0, 0, 4, 0, 0, 1, 0,
                     6, 0, 0, 5, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 7, 8, 0,
                     5, 0, 0, 0, 0, 9, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 4, 0]).reshape(9, 9)
    print(hard)
    solve_sudoku(hard)
