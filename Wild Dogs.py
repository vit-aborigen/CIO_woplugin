from itertools import combinations
from collections import defaultdict

def build_line(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    k = (y2 - y1) / ((x2 - x1) if (x2 - x1) else 1)
    b = y1 - k * x1
    return (round(k, 2), round(b, 2))

def calculate_distance(line):
    return abs(round(line[1] / (line[0] ** 2 + 1) ** 0.5, 2))

def wild_dogs(coords):
    lines = defaultdict(set)
    for p1, p2 in combinations(coords, 2):
        coef = build_line(p1, p2)
        lines[coef].update({tuple(p1), tuple(p2)})
    max_points = max([len(v) for v in lines.values()])
    longest_lines = [k for k,v in lines.items() if len(v) == max_points]
    return min((calculate_distance(line) for line in longest_lines))

if __name__ == '__main__':

    print(wild_dogs([[10,23],[4,5],[7,14],[10,110]]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
