UNTIL_TWENTY = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
AFTER_TWENTY = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = ' hundred '

def checkio(number):
    if number >= 100:
        return (UNTIL_TWENTY[number//100] + HUNDRED + convert_small_number_to_words(number - number//100*100)).strip()
    return (convert_small_number_to_words(number)).strip()


def convert_small_number_to_words(number):
    if number < 20:
        return UNTIL_TWENTY[number]
    quot, remain = divmod(number, 10)
    return AFTER_TWENTY[quot] + ' ' + UNTIL_TWENTY[remain]



if __name__ == '__main__':
    print(checkio(100))
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')