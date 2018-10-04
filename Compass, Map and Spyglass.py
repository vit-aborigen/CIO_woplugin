def navigation(seaside):
    Y, C, M, S = get_keypoint_coordinates(seaside)
    Y_to_C = calculate_distance_between_two_points(Y, C)
    Y_to_M = calculate_distance_between_two_points(Y, M)
    Y_to_S = calculate_distance_between_two_points(Y, S)
    return sum((Y_to_C, Y_to_M, Y_to_S))

def get_keypoint_coordinates(seaside):
    Y = [-1, -1]
    C = [-1, -1]
    M = [-1, -1]
    S = [-1, -1]

    for i in range(len(seaside)):
        for j in range(len(seaside[i])):
            if seaside[i][j] == 'Y':
                Y = [i, j]
            elif seaside[i][j] == 'C':
                C = [i, j]
            elif seaside[i][j] == 'M':
                M = [i, j]
            elif seaside[i][j] == 'S':
                S = [i, j]
    return (Y, C, M, S)
def calculate_distance_between_two_points(A, B):
    return max(abs(A[0] - B[0]), abs(A[1]- B[1]))

if __name__ == '__main__':

    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
