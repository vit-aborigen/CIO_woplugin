from itertools import zip_longest

def checkio(text, word):
    text_formatted = text.replace(' ', '').lower().split('\n')
    result = []
    for idx, row in enumerate(text_formatted):
        if word in row:
            spot = row.find(word)
            result = [idx + 1, spot + 1, idx + 1, spot + len(word)]
            break
    if not result:
        transposed_text = [''.join([char for char in line if char != ' ']) for line in zip_longest(*text_formatted, fillvalue='')]
        transposed_text = [nonempty for nonempty in transposed_text if nonempty]
        print(transposed_text)
        for idx, col in enumerate(transposed_text):
            if word in col:
                spot = col.find(word)
                result = [spot + 1, idx + 1, spot + len(word), idx + 1]
                break
    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("""DREAMING of apples on a wall,
# And dreaming often, dear,
# I dreamed that, if I counted all,
# -How many would appear?""", "ten") == [2, 14, 2, 16]
#     assert checkio("""He took his vorpal sword in hand:
# Long time the manxome foe he sought--
# So rested he by the Tumtum tree,
# And stood awhile in thought.
# And as in uffish thought he stood,
# The Jabberwock, with eyes of flame,
# Came whiffling through the tulgey wood,
# And burbled as it came!""", "noir") == [4, 16, 7, 16]
print(checkio("xa\nxb\nx", "ab"))