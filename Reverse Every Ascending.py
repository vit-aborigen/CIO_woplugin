def reverse_ascending(a):
    result = []
    if not a:
        return result
    elif len(a) == 1:
        return a

    buffer = [a[0]]
    for char in a[1:]:
        if char > buffer[-1]:
            buffer.append(char)
        else:
            result.extend(sorted(buffer, reverse=True))
            buffer = [char]
    result.extend(sorted(buffer, reverse=True))
    return result


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
    assert reverse_ascending([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert reverse_ascending([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert reverse_ascending([]) == []
    assert reverse_ascending([1]) == [1]
    assert reverse_ascending([1, 1]) == [1, 1]
    assert reverse_ascending([1, 1, 2]) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
