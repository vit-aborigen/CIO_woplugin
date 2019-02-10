def return_possible_moves(position, figures_left):
    neighbours = []

    # finding row neighbours
    moves_with_jumping = sorted([cell for cell in figures_left if (cell.endswith(position[1]))] + [position])
    idx = moves_with_jumping.index(position)
    if idx - 1 >= 0:
        neighbours.append(moves_with_jumping[idx-1])
    if idx + 1 < len(moves_with_jumping):
        neighbours.append(moves_with_jumping[idx + 1])

    # finding column neighbours
    moves_with_jumping = sorted([move for move in figures_left if (move.startswith(position[0]))] + [position],
                                key=lambda x: x[1])
    idx = moves_with_jumping.index(position)
    if idx - 1 >= 0:
        neighbours.append(moves_with_jumping[idx - 1])
    if idx + 1 < len(moves_with_jumping):
        neighbours.append(moves_with_jumping[idx + 1])

    return neighbours


def berserk_rook(berserker, enemies):
    def DFS(start, enemies_left, path=[]):
        path = path + [start]
        if not enemies_left:
            return path
        neighbours = return_possible_moves(start, enemies_left)
        if not neighbours:
            return path
        longest_path = []
        for cell in neighbours:
            if cell not in path:
                new_path = DFS(cell, enemies_left - {cell} - set(path), path)
                if new_path:
                    if not longest_path or len(new_path) > len(longest_path):
                        longest_path = new_path
        return longest_path

    return len(DFS(berserker, enemies)) - 1


print(berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook('d3', {'d6', 'b6', 'c8', 'g4', 'b8', 'g6'}) == 5, "one path"
    assert berserk_rook('a2', {'f6', 'f2', 'a6', 'f8', 'h8', 'h6'}) == 6, "several paths"
    assert berserk_rook('a2', {'f6', 'f8', 'f2', 'a6', 'h6'}) == 4, "Don't jump through"

