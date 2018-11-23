from datetime import date

def friday(day):
    diff = 4 - date(*map(int, day.split('.')[::-1])).weekday()
    return diff if diff >= 0 else 7 + diff

if __name__ == '__main__':
    print("Example:")
    print(friday('11.11.1111'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
