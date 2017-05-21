# Numpy based solution (checkio import issues)
# import numpy as np
#
# def checkio(matrix):
#     array = np.array(matrix)
#     transposed = -np.matrix.transpose(array)
#     return (array == transposed).all()

def checkio(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][j] == -matrix[j][i]:
                return False
    return True



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
