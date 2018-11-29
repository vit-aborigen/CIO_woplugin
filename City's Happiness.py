from collections import defaultdict

def union_find(net, city):
    net = [set(edge) if city not in edge else set(edge) - set(city) for edge in net]
    unions = []
    for edge in net:
        temp = []
        for subset in unions:
            if subset & edge:
                edge |= subset
            else:
                temp.append(subset)
        temp.append(edge)
        unions = temp
    return unions

def calculate_hapinness(graph, node, users):
    total = users[node]
    for subset in graph:
        total += sum(users[city] for city in subset) ** 2
    return total

def most_crucial(net, users):
    results = defaultdict(lambda: 0)
    for city in users:
        disjoint = union_find(net, city)
        results[city] = calculate_hapinness(disjoint, city, users)
    lowest_value = min(results.values())
    return [k for k,v in results.items() if v == lowest_value]



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')