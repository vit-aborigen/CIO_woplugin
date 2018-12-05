def count_consecutive_summers(a):
    ran = range(1, a)
    counter = 1
    for start in range(1, a//2 + 1):
        end = start + 1
        while sum(ran[start:end]) <= a and end < a:
            if sum(ran[start:end]) == a:
                counter += 1
                break
            end += 1
    return counter




if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
