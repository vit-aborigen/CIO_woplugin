def long_repeat(line):
    if line == None or not len(line): return 0
    previous_best, quantity, best_result = 0, 0, 0
    for char in line:
        if char == previous_best:
            quantity += 1
        else:
            best_result = max(quantity, best_result)
            previous_best = char
            quantity = 1
    return max(best_result, quantity)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat(None) == 0, "Empty"
    print('"Run" is good. How is "Check"?')