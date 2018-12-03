'''
Algorithm:
1) Disjoint set (start_new_colony) to distinct all separate colonies
2) Generate perfect colonies (will be used as the mask / pattern) with the [2-5] side-length with the center at (0,0) point
3) Calculate size of all perfect colonies (magic numbers)
4) Compare size of each found colony with the perfect colonies. Leave colonies that fit to magic numbers
5) Adjust


'''

from collections import deque, Counter

def generate_perfect_colonies(max_len=7):
    perfect_colonies = {}
    for size in range(1, max_len):
        perfect_colony = []
        for i in range(-size, size + 1):
            perfect_colony += [(i, j) for j in range(-size + abs(i), size - abs(i) + 1)]
        perfect_colonies[len(perfect_colony)] = perfect_colony
    return perfect_colonies

def start_new_colony(grid, start):
    neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    colony = set([start])
    frontier = deque([start])

    while frontier:
        current_i, current_j = frontier.popleft()
        for delta_i, delta_j in neighbours:
            i, j = current_i + delta_i, current_j + delta_j
            if (0 <= i < len(grid)) and (0 <= j < len(grid[0])) and grid[i][j] == 1 and ((i, j) not in colony):
                colony.add((i, j))
                frontier.append((i, j))
    return colony

def is_bacteria_belong_to_any_colony(bacteria, colonies):
    for colony in colonies:
        if bacteria in colony:
            return True
    return False

def find_central_point_of_colony(colony):
    x = Counter([dot[0] for dot in colony])
    y = Counter([dot[1] for dot in colony])


def healthy(grid):
    h, w = len(grid), len(grid[0])
    colonies = []
    perfect_colonies = generate_perfect_colonies()
    print(perfect_colonies)
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not is_bacteria_belong_to_any_colony((i,j), colonies):
                colonies.append(start_new_colony(grid, (i, j)))
    colonies = [colony for colony in colonies if len(colony) in perfect_colonies.keys()]
    return colonies

print(healthy(((0,0,0,0,0,1,0,0,0,0,1,1,0,0,0),(0,0,0,0,1,1,1,0,0,0,1,1,1,0,0),(0,0,0,0,0,1,0,0,0,1,1,1,1,1,0),(0,0,0,0,0,0,0,0,1,1,1,1,1,1,1),(0,0,0,1,0,0,0,0,0,1,1,1,1,1,0),(0,0,1,1,1,0,0,0,0,0,1,1,1,0,0),(0,1,1,1,1,1,0,0,0,0,0,1,0,0,0),(1,1,1,1,1,1,1,0,0,0,0,0,0,0,0),(0,1,1,0,1,1,0,0,0,0,1,0,0,0,0),(0,0,1,1,1,1,0,0,0,1,1,1,0,0,0),(0,0,0,1,0,0,0,0,1,1,1,1,1,0,0),(0,0,0,0,0,0,0,1,1,1,1,1,1,1,0),(0,0,0,0,0,0,0,0,1,1,1,1,1,0,0),(0,0,0,0,0,0,0,0,0,1,1,1,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))))

# def healthy(grid):
#     return 0, 0

# print(healthy(((0, 1, 0),
#          (1, 1, 1),
#          (0, 1, 0),)))

# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     def check(result, answers):
#         return list(result) in answers
#
#     check(healthy(((0, 1, 0),
#                    (1, 1, 1),
#                    (0, 1, 0),)), [[1, 1]])
#     check(healthy(((0, 0, 1, 0, 0),
#                    (0, 1, 1, 1, 0),
#                    (0, 0, 1, 0, 0),
#                    (0, 0, 0, 0, 0),
#                    (0, 0, 1, 0, 0),)), [[1, 2]])
#     check(healthy(((0, 0, 1, 0, 0),
#                    (0, 1, 1, 1, 0),
#                    (0, 0, 1, 0, 0),
#                    (0, 0, 1, 0, 0),
#                    (0, 0, 1, 0, 0),)), [[0, 0]])
#     check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
#                    (0, 0, 1, 0, 0, 1, 1, 1),
#                    (0, 1, 1, 1, 0, 0, 1, 0),
#                    (1, 1, 1, 1, 1, 0, 0, 0),
#                    (0, 1, 1, 1, 0, 0, 1, 0),
#                    (0, 0, 1, 0, 0, 1, 1, 1),
#                    (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
#     check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
#                    (0, 0, 0, 2, 2, 2, 2, 2),
#                    (0, 0, 1, 0, 0, 0, 2, 0),
#                    (0, 1, 1, 1, 0, 0, 2, 0),
#                    (1, 1, 1, 1, 1, 0, 2, 0),
#                    (0, 1, 1, 1, 0, 0, 2, 0),
#                    (0, 0, 1, 0, 0, 0, 2, 0),
#                    (0, 0, 0, 1, 0, 0, 2, 0),
#                    (0, 0, 1, 1, 1, 0, 2, 0),
#                    (0, 1, 1, 1, 1, 1, 0, 0),
#                    (0, 0, 1, 1, 1, 0, 0, 0),
#                    (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])
