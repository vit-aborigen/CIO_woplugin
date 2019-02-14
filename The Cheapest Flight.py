def cheapest_flight(costs, a: str, b: str) -> int:
    total = lambda graph, path:\
        sum([price for city_1, city_2, price in graph for start, finish in zip(path, path[1:])
             if (start == city_1 and finish == city_2) or (start == city_2 and finish == city_1)])

    def DFS(graph, start, finish, path=[]):
        path = path + [start]
        if start == finish:
            return [path]
        paths = []
        for city, cost in graph[start]:
            if city not in path:
                new_paths = DFS(graph, city, finish, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    graph = {}
    for k, v, cost in costs:
        if not graph.get(k, 0):
            graph[k] = {(v, cost)}
        if not graph.get(v, 0):
            graph[v] = {(k, cost)}
        graph[k] |= {(v, cost)}
        graph[v] |= {(k, cost)}

    result = DFS(graph, a, b)
    if not result:
        return 0
    return min([total(costs, path) for path in result])


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A'))

 #    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")