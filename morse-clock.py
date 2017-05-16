def checkio(time_string):
    hours_d, minutes_d, seconds_d = [divmod(int(time),10) for time in time_string.split(':')]

    def convert_to_bin(time: tuple):
        result = bin(time[0])[2:].zfill(3) + ' '
        result += bin(time[1])[2:].zfill(4) + ' : '
        return result

    time_bin = ''
    for time in (hours_d, minutes_d, seconds_d):
        time_bin += convert_to_bin(time)

    return time_bin[1:-3].replace('0', '.').replace('1', '-')


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
