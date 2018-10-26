from itertools import combinations
from copy import deepcopy

def is_on_same_line(three_points):
    x, y, z = three_points
    return (z[0] * (y[1] - x[1]) - z[1] * (y[0] - x[0]) == x[0] * y[1] - y[0] * x[1])

def is_subline(line_1, line_2):
    if len(line_1 - line_2) == 1:
        return True
    return False

def unite_lines(combinations):
    result = []
    for first_line in combinations:
        flag_is_checked = False
        for second_line in combinations[1:]:
            if is_subline(first_line, second_line):
                extended_line = first_line.union(second_line)
                if extended_line not in result:
                    result.append(extended_line)
                flag_is_checked = True
        if not flag_is_checked:
            result.append(first_line)
    return result

def checkio(cakes):
    all_possible_lines = []
    for three_points in combinations(cakes, 3):
        if is_on_same_line(three_points):
            all_possible_lines.append(set(tuple(point) for point in three_points))

    result = deepcopy(all_possible_lines)
    flag_all_lines_merged = False
    while not flag_all_lines_merged:
        tmp = unite_lines(result)
        if tmp == result:
            flag_all_lines_merged = True
        result = deepcopy(tmp)
    return len(result)




# print(checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2], [6,6]]))
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6