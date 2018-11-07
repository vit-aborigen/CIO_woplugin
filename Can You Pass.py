# based on https://habr.com/post/331192/

from collections import deque, defaultdict

def can_pass(matrix, first, second):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    h, w = len(matrix), len(matrix[0])
    symbol = matrix[first[0]][first[1]]
    frontier = deque([first])
    visited = set([first])

    while frontier:
        current = frontier.popleft()
        ci, cj = current
        for di, dj in directions:
            i, j = ci + di, cj + dj
            if (0 <= i < h) and (0 <= j < w) and (matrix[i][j] == symbol) and ((i,j) not in visited):
                visited.add((i, j))
                frontier.append((i, j))
    return second in visited






if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
