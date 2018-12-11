from collections import deque
from itertools import groupby

def find_structures(map, start, char):
    neighbours = [(0,1), (0,-1), (1,0), (-1,0)]
    structure = set([start])
    frontier = deque([start])

    while frontier:
        current_i, current_j = frontier.popleft()
        for delta_i, delta_j in neighbours:
            i, j = current_i + delta_i, current_j + delta_j
            if (0 <= i < len(map)) and (0 <= j < len(map[0])) and map[i][j] == char and ((i, j) not in structure):
                structure.add((i, j))
                frontier.append((i, j))
    return structure

def mark_walls(new_map, walls, char = 'S'):
    neighbours = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i | j]
    for wall in walls:
        for current_i, current_j in wall:
            for delta_i, delta_j in neighbours:
                i, j = current_i + delta_i, current_j + delta_j
                if (0 <= i < len(new_map)) and (0 <= j < len(new_map[0])) and new_map[i][j] == '.':
                    new_map[i][j] = char

def mark_dutchman(new_map, point, spaces):
    for space in spaces:
        if point in space:
            for i, j in space:
                new_map[i][j] = 'D'

def finish_map(regional_map):
    h, w = len(regional_map), len(regional_map[0])
    walls_with_duplicates = [find_structures(regional_map, (i, j), 'X') for i in range(h) for j in range(w) if regional_map[i][j] == 'X']
    walls = [wall for wall, _v in groupby(walls_with_duplicates)]
    new_map = [[char if char != 'D' else '.' for char in string] for string in regional_map]
    mark_walls(new_map, walls)
    non_marked_parts_with_duplicates = ([find_structures(new_map, (i, j), '.') for i in range(h) for j in range(w) if new_map[i][j] == '.'])
    empty_spaces = []
    [empty_spaces.append(space) for space in non_marked_parts_with_duplicates if space not in empty_spaces]
    dutchmans = [(i, j) for i in range(h) for j in range(w) if regional_map[i][j] == 'D']
    [mark_dutchman(new_map, dutchman, empty_spaces) for dutchman in dutchmans]
    result = [''.join([char if char != '.' else 'S' for char in string]) for string in new_map]
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"
