def safe_code(equation):
    equation = equation.replace('=', '==').replace('--', '+')
    variables, result = equation.split('==')
    if '*' in variables:
        var_1, var_2 = variables.split('*')
    elif '+' in variables:
        var_1, var_2 = variables.split('+')
    else:
        idx = variables.rindex('-')
        var_1 = variables[:idx]
        var_2 = variables[idx + 1:]

    for i in range(10):
        if (str(i) in equation) or (result.count('#') > 1 and not i) or \
                ((var_1.startswith('#') or var_2.startswith('#') or result.startswith('0')) and not i):
            continue

        if eval(equation.replace('#', str(i))):
            return i
    return -1

if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
