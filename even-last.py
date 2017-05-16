def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    result = 0
    size = len(array)
    if size == 0:
        return 0
    for index in range(size):
        if index%2 == 0:
            result += array[index]
    return result*array[size-1]        
            

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
