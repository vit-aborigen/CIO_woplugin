import string

def checkio(number):
    alphabet = string.digits + string.ascii_uppercase
    init = alphabet.index(max(number)) + 1
    for k in range(init, 36):
        n = int(number, k)
        if not n % (k - 1):
            return k
    return init if not int(number, init) % (init - 1) else 0



print(checkio("ZZZ"))
print(int('ZZZ', 36))

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio("18") == 10, "Simple decimal"
#     assert checkio("1010101011") == 2, "Any number is divisible by 1"
#     assert checkio("222") == 3, "3rd test"
#     assert checkio("A23B") == 14, "It's not a hex"
#     assert checkio("IDDQD") == 0, "k is not exist"
#     print('Local tests done')
