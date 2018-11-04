class Node(object):
    def __init__(self, name):
        self.name = name
        self.__population = 0

    def set_population(self, population):
        self.__population = population

    def get_population(self):
        return self.__population


    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return ord(self.name)

    def __str__(self):
        return 'Node {} with {} population'.format(self.name, self.__population)

    def __repr__(self):
        return self.name


class Graph(object):
    def __init__(self):
        self.nodes = dict()

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return

    def add_edge(self, start_node, finish_node):
        if start_node and finish_node in self.nodes:
            self.nodes[start_node].add(finish_node)

    def remove_edge(self, start_node, finish_node):
        start = self.get_node(start_node)
        finish = self.get_node(finish_node)
        self.nodes[start] -= {finish}

    def find_path(self, start, finish, path = None):
        if path == None:
            path = []
        path += start,
        if start == finish:
            return path
        for node in self.nodes[start]:
            if node not in path:
                new_path = self.find_path(node, finish, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return str(self.nodes)

    __repr__ = __str__


class Checkio_graph(Graph):

    def __init__(self):
        super(Checkio_graph, self).__init__()
        self.start = None

    def broke_connections(self, node):
        if node in self.nodes:
            for vertex in self.nodes:
                self.nodes[vertex] -= {node}
            self.nodes[node] = set()


def build_graph(net, users, source, crushes):
    graph = Checkio_graph()

    for edge in net:
        node_1, node_2 = Node(edge[0]), Node(edge[1])
        graph.add_node(node_1)
        graph.add_node(node_2)
        graph.add_edge(node_1, node_2)
        graph.add_edge(node_2, node_1)

    for k, v in users.items():
        graph.get_node(k).set_population(v)

    graph.source = graph.get_node(source)

    for node in crushes:
        broken = graph.get_node(node)
        graph.broke_connections(broken)

    return graph


def disconnected_users(*args):
    graph = build_graph(*args)
    start = graph.source
    non_connected = 0

    for finish in graph.nodes:
        if start.name in args[-1]:
            return sum([node.get_population() for node in graph.nodes])
        if graph.find_path(start, finish) == None:
            non_connected += finish.get_population()
    return non_connected



print(disconnected_users([["A","B"],["B","C"],["C","D"]],{"A":10,"C":30,"B":20,"D":40},"A",["A"]))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')