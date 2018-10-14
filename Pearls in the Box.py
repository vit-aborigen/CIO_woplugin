def checkio(marbles: str, step: int) -> float:
    b,w = marbles.count('b'), marbles.count('w')
    return 1 - round(bintree(b, w, step), 2)

def bintree(b, w, depth):
    if depth == 1:
        return b/(b+w)
    if not w:
        return bintree(b-1, w+1, depth-1)
    elif not b:
        return bintree(b+1, w-1, depth-1)
    return bintree(b-1, w+1, depth-1) * b/(b+w) + bintree(b+1, w-1, depth-1) * w/(b+w)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")