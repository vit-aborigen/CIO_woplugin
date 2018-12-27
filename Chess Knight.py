from itertools import permutations

def chess_knight(start, moves):
    directions = [v for v in permutations([-2, -1, 1, 2], 2) if (abs(v[0]) + abs(v[1]) == 3)]
    rows, columns = 'abcdefgh', '12345678'
    unchecked_positions, result = [(rows.index(start[0]), int(start[1]) - 1)], []
    for i in range(moves):
        while unchecked_positions:
            start_i, start_j = unchecked_positions.pop()
            for delta_i, delta_j in directions:
                i, j = start_i + delta_i, start_j + delta_j
                if (0 <= i <= 7 and 0 <= j <= 7) and (i,j) not in result:
                    result.append((i, j))
        unchecked_positions = result[::]
    return sorted([''.join([rows[row], columns[column]]) for row, column in result])


if __name__ == '__main__':
    print("Example:")
    print(chess_knight('h8', 2))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")