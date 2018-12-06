from collections import Counter

frequency_sort = lambda a: [k for k, v in Counter(a).most_common(len(set(a))) for _ in range(v)] if a else []



if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([1, 2, 2, 3, 3, 3]))
    print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([1, 2, 2, 3, 3, 3])) == [3, 3, 3, 2, 2, 1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
