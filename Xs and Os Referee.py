from typing import List

def checkio(game_result: List[str]) -> str:
    for row in game_result:
        if len(set(row)) == 1 and row[0] != '.':
            return row[0]
    for col in zip(*game_result):
        if len(set(col)) == 1 and col[0] != '.':
            return col[0]
    first_diag = set([game_result[i][i] for i in range(3)])
    second_diag = set([game_result[i][2-i] for i in range(3)])
    if len(first_diag) == 1 and game_result[0][0] != '.':
        return game_result[0][0]
    elif len(second_diag) == 1 and game_result[0][2] != '.':
        return game_result[0][2]
    return 'D'

print(checkio(["...","XXX","OO."]))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")