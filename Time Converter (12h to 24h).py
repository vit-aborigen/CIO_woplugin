from datetime import datetime

def time_converter(time):
    dt = datetime.strptime(time.replace('.', ''), "%I:%M %p")
    return dt.strftime("%H:%M")

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))


    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")