from datetime import time as tm

def sun_angle(time):
    dawn = tm(6, 00)
    sunset = tm(18, 00)
    h, m = map(int, time.split(':'))
    time = tm(h, m)

    if dawn <= time <= sunset:
        return (h - 6) * 15 + m / 4
    return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("14:20"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")