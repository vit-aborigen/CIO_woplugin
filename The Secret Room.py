UNTIL_20 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
            'eighteen', 'nineteen']

TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def convert_to_text(number):
    if 1 <= number < 20:
        return UNTIL_20[number - 1]
    elif 20 <= number < 100:
        return TENS[number//10 - 2] + ' ' + convert_to_text(number % 10)
    elif number == 1000:
        return 'one thousand '
    elif number == 0:
        return ''
    else:
        return UNTIL_20[number // 100 - 1] + ' hundred ' + convert_to_text(number % 100)

def secret_room(number):
    number_text = convert_to_text(number)
    all_numbers = sorted([convert_to_text(i) for i in range(1, number+1)])
    return all_numbers.index(number_text) + 1

if __name__ == '__main__':
    print("Example:")
    print(secret_room(818))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert secret_room(5) == 1 #five, four, one, three, two
    # assert secret_room(3) == 2 #one, three, two
    # assert secret_room(1000) == 551
    # print("Coding complete? Click 'Check' to earn cool rewards!")
