import string
from itertools import groupby

RED_WORDS = ['asap', 'help', 'urgent']

def is_stressful(subj):
    if subj.endswith('!!!') or subj.isupper():
        return True
    temp_str = [letter for letter in subj.lower() if letter in string.ascii_letters]
    formatted_str = ''.join(c for c, _ in groupby(temp_str))

    return any([word for word in RED_WORDS if word in formatted_str])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HeeeeeElllLP") == True, "Second"
    print('Done! Go Check it!')