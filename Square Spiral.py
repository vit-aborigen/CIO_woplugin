add = lambda x,y: [x[0] + y[0], x[1] + y[1]]

def find_distance(first, second):
    number_coordinates = [0, 0]
    directions = [[-1,0], [0,1], [1, 0], [0, -1]]
    current_direction, max_number = 0, max(first, second)
    numbers_per_step, current_number = 1, 1
    is_direction_used_twice = False
    spiral = {}

    while current_number <= max_number:
        for i in range(1, numbers_per_step + 1):
            spiral[current_number] = number_coordinates
            number_coordinates = add(number_coordinates, directions[current_direction % 4])
            current_number += 1
        current_direction += 1
        if is_direction_used_twice:
            numbers_per_step += 1
        is_direction_used_twice = not is_direction_used_twice

    x1, y1 = spiral[first]
    x2, y2 = spiral[second]
    return abs(x1 - x2) + abs(y1 - y2)

print(find_distance(26, 31))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
