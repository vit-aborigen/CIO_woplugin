def reverse_roman(roman_string):

    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    order = 'IVXLCDM'
    result = 0
    previous_char = roman_string[0]
    counted = False

    if len(roman_string) == 1:
        return numbers[roman_string]

    for current_char in roman_string[1:]:
        if order.find(previous_char) < order.find(current_char):
            result += numbers[current_char] - numbers[previous_char]
            counted = True
        elif counted:
            counted = False
            previous_char = current_char
            continue
        else:
            result += numbers[previous_char]
        previous_char = current_char
    if not counted:
        result += numbers[current_char]
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!')