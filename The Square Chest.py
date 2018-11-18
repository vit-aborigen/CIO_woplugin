from typing import List
GRID_SIZE = 4

def all_possible_solutions(n):
    side = n - 1
    result = []
    while side:
        for start in range(1, n - side + 1):
            for end in range(n - side):
                delta = range(side + 1)
                top =    [(start + x + end * n, start + y + end * n) for x, y in zip(delta, delta[1:])]
                bottom = [(start + x + end * n + n * side, start + y + end * n + n * side) for x, y in zip(delta, delta[1:])]
                left =   [(start + x * n + end * n, start + y * n + end * n) for x, y in zip(delta, delta[1:])]
                right =  [(start + x * n + end * n + side, start + y * n + end * n + side) for x, y in zip(delta, delta[1:])]
                yield top + bottom + left + right
        side -= 1

def checkio(lines_list: List[List[int]]) -> int:
    lines_list = {tuple(sorted(v)) for v in lines_list}
    counter = [(set(square) - lines_list) for square in all_possible_solutions(GRID_SIZE)]
    return counter.count(set())


print(checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]))

if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")