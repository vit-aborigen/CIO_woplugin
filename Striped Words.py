import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def filter_string(text):
    text = re.sub('[!@#$,.?]', ' ', text)
    for word in text.upper().split():
        if len(word) > 1 and all(letter.isalpha() for letter in word):
            yield word

def checkio(text):
    counter = 0
    for word in filter_string(text):
        counter += all([1 if (pair[0] in VOWELS and pair[1] in CONSONANTS) or \
                (pair[0] in CONSONANTS and pair[1] in VOWELS) else 0 for pair in zip(word, word[1:])])
    return counter


#These "asserts" using only for self-checking and not necessary for auto-testing
print(checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?"))
#
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
