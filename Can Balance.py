from typing import Iterable

def can_balance(weights: Iterable) -> int:
    left, right = [], []
    weight = lambda x: sum([x[i] * (len(x) - i) for i in range(len(x))])
    while len(weights) > 1:
        if weight(left) > weight(right):
            right.append(weights.pop())
        else:
            left.append(weights.pop(0))
    if weight(left) == weight(right):
        return len(left)
    return -1


if __name__ == '__main__':
    print("Example:")
    print(can_balance([1,1,1,9,1,1,1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert can_balance([6, 1, 10, 5, 4]) == 2
    assert can_balance([10, 3, 3, 2, 1]) == 1
    assert can_balance([7, 3, 4, 2, 9, 7, 4]) == -1
    assert can_balance([42]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")