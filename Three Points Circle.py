from math import sqrt

def checkio(string):
    # Solution was taken from http://mathforum.org/library/drmath/view/54323.html
    v1 = (int(string[1]), int(string[3]))
    v2 = (int(string[7]), int(string[9]))
    v3 = (int(string[13]), int(string[15]))

    bx, by = v1
    cx, cy = v2
    dx, dy = v3

    temp = cx**2 + cy**2
    bc = (bx**2 + by**2 - temp) / 2
    cd = (temp - dx**2 - dy**2) / 2
    det = (bx - cx) * (cy - dy) - (cx - dx) * (by - cy)

    if abs(det) < 1.0e-6:
        return

    # Center of circle
    det = 1 / det
    xw = (bc * (cy - dy) - cd * (by - cy)) * det
    yw = ((bx - cx) * cd - (cx - dx) * bc) * det
    radius = sqrt((xw - bx) ** 2 + (yw - by) ** 2)

    f = lambda x: str(round(x, 2)).rstrip('0').rstrip('.')
    result = map(f, [xw, yw, radius])
    return '(x-{})^2+(y-{})^2={}^2'.format(*result)


print(checkio("(2,2),(6,2),(2,6)"))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
