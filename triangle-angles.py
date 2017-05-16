import math
def checkio(a, b, c):
    if (a+b <=c) or (a+c<=b) or (b+c<=a):
        return[0,0,0]
    alpha = int(round(math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b))), 0))
    beta = int(round(math.degrees(math.acos((c**2 + b**2 - a**2)/(2*c*b))), 0))
    gamma = int(round(math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c))), 0))
    return sorted([alpha, beta, gamma])

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"