import operator

def checkio(first, second):
    first_str = bin(first)[2:]
    second_str = bin(second)[2:]
    result = 0

    tmp = ''
    operators = [operator.xor, operator.and_, operator.or_]
    for op in operators:
        for i in range(len(first_str)):
            tmp = ''
            for j in range(len(second_str)):
                tmp += str(op(int(first_str[i], 2), int(second_str[j])))
            result += int(''.join(tmp), 2)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18