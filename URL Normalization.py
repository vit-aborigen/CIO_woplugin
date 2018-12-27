from itertools import chain

def checkio(url):
    percent_positions = list(chain(*[(idx + 1, idx + 2) for idx, char in enumerate(url) if char == '%' if idx <= len(url) - 3]))
    convert_to_lowercase = lambda x: x.lower()
    capitalize_letters_in_escape_seq = lambda x: [char if idx not in percent_positions else char.upper() for idx, char in enumerate(x)]

    first_rule = convert_to_lowercase(url)
    second_rule = capitalize_letters_in_escape_seq(first_rule)
    third_rule = decode_octets(second_rule, percent_positions)
    fourth_rule = ''.join(third_rule).replace(':80/', '')
    print(fourth_rule)
    return fourth_rule


def decode_octets(url, positions):
    for value in positions[::2]:
        char_ascii = url[value] + url[value+1]
        char = chr(int(char_ascii, 16))
        if char in ['-', '.', '_', '~'] or char.isalnum():
            url[value-1:value+2] = ('2del', char, '2del')
    return filter(lambda a: a != '2del', url)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("Http://Www.Checkio.org") == \
    #     "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')