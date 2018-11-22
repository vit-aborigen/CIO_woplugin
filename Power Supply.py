def build_graph(network):
    graph = {}
    for node_1, node_2 in network:
        if node_1 not in graph:
            graph[node_1] = set()
        if node_2 not in graph:
            graph[node_2] = set()

        graph[node_1].add(node_2)
        graph[node_2].add(node_1)
    return graph

def power_supply(network, power_plants):
    def find_path(start, end, path = None):
        if not path:
            path = []
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return False

        shortest_path = None
        for node in graph[start]:
            if node not in path:
                new_path = find_path(node, end, path)
                if new_path:
                    if not shortest_path or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        return shortest_path

    graph = build_graph(network)
    has_connection = set()
    for city in graph:
        if city in power_plants or city in has_connection:
            continue
        for plant in power_plants:
            path = find_path(city, plant)
            if len(path) <= power_plants[plant] + 1:
                has_connection.add(city)
    return set(graph) - has_connection - set(power_plants)

print(power_supply([["p1","c2"],["c2","c3"],["c3","c4"],["c4","p5"],["c6","c7"],["c7","c8"],["c8","c9"],["c9","c10"],["c11","c12"],["c12","c13"],["c13","c14"],["c14","c15"],["c16","c17"],["c17","c18"],["c18","c19"],["c19","c20"],["p21","c22"],["c22","c23"],["c23","c24"],["c24","p25"],["p1","c6"],["c2","c7"],["c3","c8"],["c4","c9"],["p5","c10"],["c6","c11"],["c7","c12"],["c8","c13"],["c9","c14"],["c10","c15"],["c11","c16"],["c12","c17"],["c13","c18"],["c14","c19"],["c15","c20"],["c16","p21"],["c17","c22"],["c18","c23"],["c19","c24"],["c20","p25"]],{"p25":3,"p1":3,"p21":3,"p5":3}))

# if __name__ == '__main__':
#     assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['c2']), 'one blackout'
#     assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3']), 'two blackout'
#     assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([]), 'no blackout'
#     assert power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0}) == set(['c0', 'c2']), 'weak power-plant'
#     assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}) == set([]), 'cooperation'
#     assert power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
#                          ['c5', 'c6'], ['c5', 'p7']],
#                         {'p1': 1, 'p7': 1}) == set(['c3', 'c4', 'c6']), 'complex cities 1'
#     assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
#                          ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
#                        ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
#                        ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
#                       {'p0': 1, 'p12': 4, 'p8': 1}) == set(['c6', 'c7']), 'complex cities 2'
#     assert power_supply([['c1', 'c2'], ['c2', 'c3']], {}) == set(['c1', 'c2', 'c3']), 'no power plants'
#     assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}) == set(['c3']), 'circle'
#     assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}) == set([]), 'more than enough'
#     print("Looks like you know everything. It is time for 'Check'!")