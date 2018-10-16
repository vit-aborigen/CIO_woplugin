def build_graph(numbers):
    def is_diff_by_one_digit(digit1, digit2, size=3):
        return sum(str(digit1)[i] != str(digit2)[i] for i in range(size)) == 1

    graph = {k: set() for k in numbers}
    for number in numbers:
        for node in numbers:
            if is_diff_by_one_digit(number, node):
                graph[number].add(node)
    return graph

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def checkio(numbers):
    graph = build_graph(numbers)
    return find_shortest_path(graph, numbers[0], numbers[-1])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"


