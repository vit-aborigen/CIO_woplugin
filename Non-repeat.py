def non_repeat(line):
    temp_longest, current_longest = '', ''
    for char in line:
        if char in temp_longest:
            current_longest = max(current_longest, temp_longest, key=lambda x: len(x))
            index_of_repeating_symbol = temp_longest.index(char) + 1
            temp_longest = temp_longest[index_of_repeating_symbol:] + char
        else:
            temp_longest += char
    return max(current_longest, temp_longest, key=lambda x: len(x))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')