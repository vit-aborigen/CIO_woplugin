TRIANGLE_NUMBERS_AMOUNT = 50

def checkio(number):
    if number == 0: return []
    triangle_numbers = [(i ** 2 + i) // 2 for i in range(1, TRIANGLE_NUMBERS_AMOUNT)]
    temporary_sum = 0

    for idx in range(TRIANGLE_NUMBERS_AMOUNT-1):
        spotted_counter = 1
        temporary_sum = triangle_numbers[idx]
        while temporary_sum <= number:
            if temporary_sum == number:
                return triangle_numbers[idx:idx+spotted_counter]
            temporary_sum += triangle_numbers[idx + spotted_counter]
            spotted_counter += 1
    return []





# def checkio(number):
#     return [number // 2, number - number // 2]
#
# #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"