def is_palindromic(string):
    return string == string[::-1]

def longest_palindromic(text):
    text_len = len(text)
    while text_len:
        for i in range(len(text) - text_len + 1):
            if is_palindromic(text[i:i + text_len]):
                return text[i:i + text_len]
        text_len -= 1

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"