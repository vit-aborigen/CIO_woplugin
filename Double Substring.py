import re

def double_substring(line):
    if line == None or len(line) < 2: return 0
    elif len(line) == 2: return 1

    found_substrings = -1
    search_range = 2
    while found_substrings not in (0,1):
        for i in range(len(line) - search_range):
            current_substring = line[i:i+search_range]
            found_substrings = len([substr.start() for substr in re.finditer(current_substring, line)])
            if found_substrings > 1:
                search_range += 1
                break

    return 0 if search_range-1 == 1 else search_range-1

print(double_substring('aa'))

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert double_substring('aaaa') == 2, "First"
#     assert double_substring('abc') == 0, "Second"
#     assert double_substring('aghtfghkofgh') == 3, "Third"
#     print('"Run" is good. How is "Check"?')