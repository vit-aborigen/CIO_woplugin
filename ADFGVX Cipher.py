from itertools import zip_longest
adfgvx = "ADFGVX"

def encode(message, secret_alphabet, keyword):
    n = len(adfgvx)
    fractionated_form = []
    for letter in [char for char in message.lower() if char.isalnum()]:
        i, j = divmod(secret_alphabet.find(letter), n)
        fractionated_form.extend([adfgvx[i], adfgvx[j]])

    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    n = len(keyword)
    table = [list(fractionated_form[i:i + n]) for i in range(0, len(fractionated_form), n)]

    dic = {}
    for k, v in enumerate(zip_longest(*table, fillvalue='')):
        if keyword[k] not in dic:
            dic[keyword[k]] = v
    return ''.join([''.join(dic[k]) for k in sorted(keyword)])


def decode(message, secret_alphabet, keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    short_word_len, starting_from  = divmod(len(message), len(keyword))
    dic_len = {v:(short_word_len if v in keyword[starting_from:] else short_word_len + 1) for v in keyword}
    dic, start = {}, 0
    for letter in sorted(keyword):
        end = start + dic_len[letter]
        dic[letter] = message[start:end]
        start = end

    coded = ''.join([''.join(code) for code in zip_longest(*[dic[letter] for letter in keyword], fillvalue='')])
    fractionated_form = [coded[i:i+2] for i in range(0, len(coded), 2)]
    result = ''
    for row, column in fractionated_form:
        i, j = adfgvx.index(row), adfgvx.index(column)
        idx = i * len(adfgvx) + j
        result += secret_alphabet[idx]
    return result


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"