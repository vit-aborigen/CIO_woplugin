from itertools import permutations
ROWS, COLUMNS = 'abcdefgh', '12345678'

def build_graph():
    graph = {row+column:set() for row in ROWS for column in COLUMNS}
    directions = [v for v in permutations([-2, -1, 1, 2], 2) if (abs(v[0]) + abs(v[1]) == 3)]

    for row, col in graph:
        for delta_i, delta_j in directions:
            new_row = chr(ord(row) + delta_i)
            new_col = str(int(col) + delta_j)
            if new_row in ROWS and new_col in COLUMNS:
                graph[row+col] |= {new_row+new_col}
    return graph

def checkio(cells):
    '''
    1) Build graph where every chess cell is a node
    2) Add edges, which are calculated as possible knight's step from a current cell
    3) BFS for finding the shortest path
    '''
    graph = build_graph()
    start, end = cells.split('-')
    frontier = [start]
    visited = {start: 0}
    while frontier:
        cell = frontier.pop(0)
        for node in graph[cell]:
            if node == end:
                visited[node] = visited[cell] + 1
                return visited[node]
            if node not in visited:
                frontier.append(node)
                visited[node] = visited[cell] + 1

print(checkio("h1-g2"))

# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio("b1-d5") == 2, "1st example"
#     assert checkio("a6-b8") == 1, "2nd example"
#     assert checkio("h1-g2") == 4, "3rd example"
#     assert checkio("h8-d7") == 3, "4th example"
#     assert checkio("a1-h8") == 6, "5th example"