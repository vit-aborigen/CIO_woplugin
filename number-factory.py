def checkio(number):
    if number < 10:
        return 0
    result = int(''.join(map(str,divide(number))))
    return result

def divide(number:int):
    result = []
    while number > 9:
        isFound = False
        for i in range(9,1,-1):
            if number%i == 0:
                isFound = True
                result += i,
                number //= i
                break
        if not isFound:
            return 0,
    result += number,
    return result[::-1]