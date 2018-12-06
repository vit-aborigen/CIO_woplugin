from collections import defaultdict

def clean_data(data):
    words = []
    for word in data:
        tmp = ''
        for char in word:
            if char not in tmp:
                tmp += char
        words += tmp,
    return words

def build_graph(words):
    graph = defaultdict(set)
    for word in words:
        for char_1, char_2 in zip(word, word[1:]):
            graph[char_1] |= {char_2}
        graph[word[-1]] |= set()
    return graph

def topo_sort(graph):
    incoming_edges = {}
    for k, v in graph.items():
        if k not in incoming_edges:
            incoming_edges[k] = 0
        for char in v:
            incoming_edges[char] = incoming_edges.get(char, 0) + 1

    empty = {k for k, v in incoming_edges.items() if not v}
    result = []

    while empty:
        char = min(empty)
        empty.remove(char)
        result.append(char)

        for neighbor in graph.get(char, set()):
            incoming_edges[neighbor] -= 1
            if not incoming_edges[neighbor]:
                empty.add(neighbor)

    return result

def checkio(data):
    words = clean_data(data)
    graph = build_graph(words)
    return ''.join(topo_sort(graph))


if __name__ == '__main__':

    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    # assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
    #     "Paste in"
    # assert checkio(["a", "b", "c"]) == "abc", \
    #     "Cant determine the order - use english alphabet"
    # assert checkio(["aazzss"]) == "azs", \
    #     "Each symbol only once"
    # assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
    #     "Concatenate and paste in"

    # print(checkio(["hfecba","hgedba","hgfdca"]), 'hgfedcba')
    # print(checkio(["ghi","abc","def"]), 'abcdefghi')
    # print(checkio(["axton","axtom","axtob"]), 'axtobmn')
    # print(checkio(["axton","bxton"]), 'abxton')
    # print(checkio(["acb", "bd", "zwa"]), 'zwacbd')
    # print(checkio(["dfg", "frt", "tyg"]), 'dfrtyg')