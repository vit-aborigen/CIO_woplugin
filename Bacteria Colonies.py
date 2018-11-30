from collections import deque

def generate_perfect_colonies(max_len=9):
    pass

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

def healthy(grid):
    h, w = len(grid), len(grid[0])
    colonies = []
    perfect_colonies = generate_perfect_colonies()
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not is_bacteria_belong_to_any_colony((i,j), colonies):
                colonies.append(start_new_colony(grid, (i, j)))

    return colonies


# def healthy(grid):
#     return 0, 0

print(healthy(((0, 1, 0),
         (1, 1, 1),
         (0, 1, 0),)))

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
