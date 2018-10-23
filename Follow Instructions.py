def follow(instructions):
    forward_backward = [1 if char == 'f' else -1 for char in instructions if char in 'fb']
    left_right = [1 if char == 'r' else -1 for char in instructions if char in 'lr']
    return (sum(left_right), sum(forward_backward))


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")