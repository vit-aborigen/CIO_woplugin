from math import pi, asin, sqrt, log

def checkio(height, width):
    c, a = height/2, width/2

    e = sqrt(1 - c**2/a**2) if c <= a else sqrt(1 - a**2/c**2)
    if c < a:
        area = 2 * pi * a ** 2 + pi * c**2 / e * log((1+e)/(1-e))
    elif c == a:
        area = 4 * pi * c**2
    else:
        area = 2*pi*a**2 * (1 + c/(a*e) * asin(e))

    volume = 4*pi/3 * c*a**2
    return [round(volume, 2), round(area, 2)]

print(checkio(4, 2))
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"