import copy
DOMINO_MAX_VALUE = 6
DEBUG = False

def log(string):
    if DEBUG:
        if isinstance(string[0], list):
            for text in string:
                print(text)
            print()
        else:
            print(string)

def build_matrix(tiles):
    matrix = [[0 for _ in range(DOMINO_MAX_VALUE + 1)] for _ in range(DOMINO_MAX_VALUE + 1)]
    for domino in tiles.split(', '):
        i, j = map(int, domino.split('-'))
        matrix[i][j] = matrix[j][i] = 1
    log(matrix)
    return matrix

def check_solution(row, source_matrix):
    if not sum(sum(row) for row in source_matrix):
        return 1
    solutions_count = 0

    for index in range(DOMINO_MAX_VALUE + 1):
        log('row: {}, index: {}, value: {}'.format(row, index, source_matrix[row][index]))
        if source_matrix[row][index]:
            source_matrix[row][index] = source_matrix[index][row] = 0
            solutions_count += check_solution(index, source_matrix)
            source_matrix[row][index] = source_matrix[index][row] = 1
    return solutions_count

def domino_chain(tiles: str) -> int:
    matrix = build_matrix(tiles)
    counter = 0
    for row in range(DOMINO_MAX_VALUE + 1):
        counter += check_solution(row, matrix)
    return counter // 2


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(domino_chain("1-2, 0-1, 2-6, 0-0, 5-5, 6-6, 5-6, 4-4, 0-6, 1-5, 1-1, 1-6, 0-5, 3-6, 0-4, 2-5, 2-4"))
    # assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    # assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    # assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    # assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    # assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    # assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    # assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    # assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    # assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    # assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    # assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    # print("Basic tests passed.")