def build_graph(dominos):
    graph = {(domino[0] + domino[2]): set() for domino in dominos.replace(',', '').split(' ')}  # Build nodes only
    connected_nodes = []
    for domino_value in range(7):
        connected_nodes.append({node for node in graph if str(domino_value) in node})  # Make a link between edges

    for nodes in filter(lambda x: len(x) > 1, connected_nodes):
        for node in nodes:
            graph[node] = graph[node].union((nodes - {node}))  # Add edges between nodes
    return graph

def remove_edges(graph, tile):
    pass


def find_all_paths(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(graph):
        yield path
    if start not in graph:
        return

    for node in graph[start]:
        if node not in path:
            yield from find_all_paths(graph, node, path)


def domino_chain(tiles: str) -> int:
    graph = build_graph(tiles)
    print(graph)
    pathes = []
    for node in graph:
        for path in find_all_paths(graph, node):
            if path[::-1] not in pathes:
                pathes.append(path)
    print(pathes)
    # return sum([1 for node in graph for path in find_all_paths(graph, node)])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # print(domino_chain("1-5, 2-5, 3-5, 4-5, 3-4"))
    # assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
    # assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
    assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    # assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6
    # assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    # assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    # assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    # assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    # assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    # assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    # assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    # print("Basic tests passed.")