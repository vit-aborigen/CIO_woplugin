def square_board(side: int, token: int, steps: int):
    directions, current_direction = [[0, -1], [-1,0], [0, 1], [1, 0]], 0
    i, j, current_value = side - 1, side - 1, 0
    max_value = 2 * side + 2 * (side - 2)
    goal = abs((steps + token) % max_value)
    while current_value != goal:
        i += directions[current_direction][0]
        j += directions[current_direction][1]
        current_value += 1
        if not current_value % (side - 1):
            current_direction = (current_direction + 1) % 4
    return (i,j)





if __name__ == '__main__':
    print("Example:")
    print(square_board(6, 2, -3))
    # assert square_board(4, 1, 4) == (1, 0)
    # assert square_board(6, 2, -3) == (4, 5)
    #
    # print("Coding complete? Click 'Check' to earn cool rewards!")