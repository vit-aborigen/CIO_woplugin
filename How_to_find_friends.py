def check_connection(network, first, second):
    graph = build_graph(network)

    def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return True

        if not start in graph.keys():
            return False

        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return False

    return find_path(graph, first, second)

def build_graph(network):
    graph = {}
    for pair in network:
        node1, node2 = pair.split('-')
        if node1 not in graph:
            graph[node1] = list(set([node2]))
        else:
            graph[node1].append(node2)

        if node2 not in graph:
            graph[node2] = list(set([node1]))
        else:
            graph[node2].append(node1)

    return graph

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

