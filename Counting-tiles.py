import math

def checkio(radius):
    length = int(math.ceil(radius))
    for i in range(length):
        for j in range(length):



checkio(2.1)
#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(2) == [4, 12], "N=2"
#     assert checkio(3) == [16, 20], "N=3"
#     assert checkio(2.1) == [4, 20], "N=2.1"
#     assert checkio(2.5) == [12, 20], "N=2.5"