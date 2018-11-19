import numpy as np
from itertools import groupby

def find_most_spotted_seq(line):
    return max(len(list(v)) for k, v in groupby(line))

def checkio(matrix):
    for row in matrix:
        if find_most_spotted_seq(row) >= 4:
            return True

    for column in zip(*matrix):
        if find_most_spotted_seq(column) >= 4:
            return True

    size = len(matrix)
    array = np.array(matrix)
    main_diagonals = [list(array.diagonal(i)) for i in range(-size + 1, size) if len(array.diagonal(i)) > 3]
    for diagonal in main_diagonals:
        if find_most_spotted_seq(diagonal) >= 4:
            return True

    antidiagonals = [list(np.flip(array, 0).diagonal(i)) for i in range(-size + 1, size) if len(array.diagonal(i)) > 3]
    for anidiagonal in antidiagonals:
        if find_most_spotted_seq(anidiagonal) >= 4:
            return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
