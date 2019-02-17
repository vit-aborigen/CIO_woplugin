from heapq import heappop, heappush

def useless_flight(schedule):
    result = []
    for idx, (start, stop, cost) in enumerate(schedule):
        if cheapest_flight(schedule, start, stop) < cost:
            result.append(idx)
    return result

def cheapest_flight(costs, start, end):
    graph = {}
    for k, v, cost in costs:
        if not graph.get(k, 0):
            graph[k] = {(v, cost)}
        if not graph.get(v, 0):
            graph[v] = {(k, cost)}
        graph[k] |= {(v, cost)}
        graph[v] |= {(k, cost)}

    frontier = [(0, start)]
    cost_so_far = {start: 0}
    while frontier:
        price, current = heappop(frontier)
        if current == end:
            return price
        for next, add_price in graph[current]:
            new_price = cost_so_far[current] + add_price
            # Kurosawa optimization
            if new_price < cost_so_far.get(next, 9999999999):
                cost_so_far[next] = new_price
                heappush(frontier, (new_price, next))

if __name__ == '__main__':
    print("Example:")
    print(useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 100]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 100]]) == [2]
    assert useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 90]]) == []
    assert useless_flight([['A', 'B', 50],
  ['B', 'C', 40],
  ['A', 'C', 40]]) == []
    assert useless_flight([['A', 'C', 10],
  ['C', 'B', 10],
  ['C', 'E', 10],
  ['C', 'D', 10],
  ['B', 'E', 25],
  ['A', 'D', 20],
  ['D', 'F', 50],
  ['E', 'F', 90]]) == [4, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")