from collections import Counter
from itertools import zip_longest

def isometric_strings(str1: str, str2: str) -> bool:
    source = Counter(str1)
    result = Counter(str2)
    return all([1 if val_1[1] == val_2[1] else 0 for val_1, val_2 in zip_longest(source.most_common(), result.most_common(), fillvalue=[0,0])])

if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('foo', 'bar'))

    # # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
