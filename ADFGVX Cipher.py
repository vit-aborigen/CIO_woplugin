from itertools import zip_longest, groupby
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
    return message


decode("FXGAFVXXAXDDDXGA", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "cipher")


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    # assert decode("FXGAFVXXAXDDDXGA",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    # assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    # assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
    #               "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
    #               "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    # assert decode("DXGAXAAXXVDDFGFX",
    #               "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
    #               "weasel") == 'iamgoing', "decode weasel == weasl"