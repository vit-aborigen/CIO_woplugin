from collections import Counter
from string import ascii_lowercase

def checkio(text: str) -> str:
    formatted_text = [char for char in text.lower() if char in ascii_lowercase]
    most_spotted = Counter(formatted_text).most_common()[0][1]
    most_common = [letter for letter, count in Counter(formatted_text).most_common() if count == most_spotted]
    return min(most_common)

if __name__ == '__main__':
    print("Example:")
    print(checkio("reb"))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")