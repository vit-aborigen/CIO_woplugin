from typing import List
from collections import deque

DIRECTIONS = [(i,j) for i in range(-1,2) for j in range(-1, 2) if i|j]

def start_new_island(land_map, start):
    island = set([start])
    frontier = deque([start])

    while frontier:
        current_i, current_j = frontier.popleft()
        for delta_i, delta_j in DIRECTIONS:
            i, j = current_i + delta_i, current_j + delta_j
            if (0 <= i < len(land_map)) and (0 <= j < len(land_map[0])) and land_map[i][j] and ((i, j) not in island):
                island.add((i, j))
                frontier.append((i, j))
    return island

def is_point_in_any_island(point, islands):
    for island in islands:
        if point in island:
            return True
    return False

def checkio(land_map: List[List[int]]) -> List[int]:
    h, w = len(land_map), len(land_map[0])
    islands = []
    for i in range(h):
        for j in range(w):
            if land_map[i][j] and not is_point_in_any_island((i,j), islands):
                islands.append(start_new_island(land_map, (i, j)))
    return sorted([len(island) for island in islands])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")