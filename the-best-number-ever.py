def checkio():
    return 42  # Answer to the Ultimate Question of Life, the Universe, and Everything

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))
