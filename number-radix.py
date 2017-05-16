def getAlpabet(radix:int):
    if radix > 37:
        return {}
    alphabet = {}
    for number in range(radix):
        if number > 9:
            alphabet[chr(55 + number)] = number
        else:
            alphabet[str(number)] = number
    return alphabet

def checkio(str_number, radix):
    base = 0
    result = 0
    alphabet = getAlpabet(radix)
    for digit in str_number[::-1]:
        if digit not in alphabet:
            return -1
        result += alphabet[digit] * radix**base
        base += 1
    return result