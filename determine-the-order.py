def checkio(data):
    letters = []
    for element in data:
        letters += [letter for letter in element if letter not in letters]


    def remove_from_matrix(matrix, letter):
        pass



checkio(["acb", "bd", "zwa"])

#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
#         "Just concatenate it"
#     assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
#         "Paste in"
#     assert checkio(["a", "b", "c"]) == "abc", \
#         "Cant determine the order - use english alphabet"
#     assert checkio(["aazzss"]) == "azs", \
#         "Each symbol only once"
#     assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
#         "Concatenate and paste in"
