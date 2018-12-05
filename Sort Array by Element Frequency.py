from collections import Counter

def frequency_sort(a):
    if not a:
        return []
    if isinstance(a[0], list):
        return frequency_sort(a[0])

    freq = Counter(a)
    return [k for k,v in freq.items() for _ in range(v)]


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([[1,2,2,1]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([['bob', 'bob', 'carl', 'alex', 'bob']])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
