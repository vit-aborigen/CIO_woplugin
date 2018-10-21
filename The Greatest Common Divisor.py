from operator import and_
from functools import reduce

def integer_factorization(value):
    return set(([value//idx for idx in range(1, value + 1) if not value % idx]))

def greatest_common_divisor(*args):
    if all([not(value % min(args)) for value in args]):
        return min(args)
    return max(reduce(and_, (map(integer_factorization, args))))


if __name__ == '__main__':
    print(greatest_common_divisor(4294967296,2))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"