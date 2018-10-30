class Node(object):
    def __init__(self, name):
        self.name = name
        self.population = 0

    def set_population(self, population):
        self.population = population

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return ord(self.name)

    def __str__(self):
        return 'Node {} with {} population'.format(self.name, self.population)

    def __repr__(self):
        return self.name


class Graph(object):
    def __init__(self):
        self.nodes = dict()
        self.source = None

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    def add_edge(self, start_node, finish_node):
        if start_node and finish_node in self.nodes:
            self.nodes[start_node].add(finish_node)

    def broke_connections(self, node):
        if node in self.nodes:
            self.nodes[node] = set()

    def __str__(self):
        return str(self.nodes)

    __repr__ = __str__

def build_graph(net, users, source, crushes):
    graph = Graph()

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

    return '-----'






print(disconnected_users([
    ['A', 'B'],
    ['B', 'C'],
    ['C', 'D']
], {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40
},
    'A', ['C']))