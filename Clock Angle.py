def clock_angle(time):
    h, m = map(int, time.split(':'))
    h_angle = 360 / 12 * (h % 12 + m / 60)
    m_angle = 360 / 60 * m
    angle = abs(h_angle - m_angle)
    return min(angle, 360 - angle)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
