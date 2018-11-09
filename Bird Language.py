VOWELS = "aeiouy"

def translate(phrase):
    result = ''
    idx = 0
    while idx != len(phrase):
        if phrase[idx] == ' ':
            result += ' '
        elif phrase[idx] in VOWELS:
            result += phrase[idx]
            idx += 2
        else:
            result += phrase[idx]
            idx += 1
        idx += 1
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
