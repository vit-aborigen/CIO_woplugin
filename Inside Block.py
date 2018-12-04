# from matplotlib import path as p
# is_inside = lambda x,y: p.Path(x).contains_point(y)

def check_point(polygon, point):
    x, y = point
    counter = 0
    side_1_x, side_1_y = polygon[0]
    for i in range(1, len(polygon)):
        side_2_x, side_2_y = polygon[i]
        if min(side_1_y, side_2_y) < y <= max(side_1_y, side_2_y) and x <= max(side_1_x, side_2_x):
            if side_1_y != side_2_y:
                tmp = (y - side_1_y) * (side_2_x - side_1_x) / (side_2_y - side_1_y) + side_1_x
            if (side_1_x == side_2_x) or (x <= tmp):
                counter += 1
        side_1_x, side_1_y = side_2_x, side_2_y
    return [False, True][counter % 2]

def is_inside(polygon, point):
    epsilon = 0.000001
    x, y = point
    points = [(x - epsilon, y), (x + epsilon, y), (x, y - epsilon), (x, y + epsilon), (x - epsilon, y - epsilon),
              (x + epsilon, y + epsilon), (x - epsilon, y + epsilon), (x + epsilon, y - epsilon), (x, y)]
    result = [check_point(polygon, dot) for dot in points]
    print(result)
    return any(result)

print(is_inside(((1,1),(1,3),(3,3),(3,1)),(1,1)))
print(is_inside(((1,1),(2,3),(1,3),(3,4),(5,3),(4,3),(3,1)),(1,2)))

# if __name__ == '__main__':
#     assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
#                      (2, 2)) == True, "First"
#     assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
#                      (4, 2)) == False, "Second"
#     assert is_inside(((1, 1), (4, 1), (2, 3)),
#                      (3, 2)) == True, "Third"
#     assert is_inside(((1, 1), (4, 1), (1, 3)),
#                      (3, 3)) == False, "Fourth"
#     assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
#                      (4, 3)) == True, "Fifth"
#     assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
#                      (4, 3)) == False, "Sixth"
#     assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
#                      (3, 3)) == True, "Seventh"
#     assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
#                      (4, 3)) == False, "Eighth"