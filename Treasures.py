def treasures(info, limit):
    processed_info = {item:value['price']/value['weight'] for item, value in info.items()}
    result = {}
    limit_left = limit * 1000
    for key, value in sorted(processed_info.items(), key=lambda k: k[1], reverse=True):
        if info[key]['amount'] * info[key]['weight'] < limit_left:
            result[key] = info[key]['amount']
            limit_left -= info[key]['amount'] * info[key]['weight']
            continue
        else:
            amount = limit_left // info[key]['weight']
            if amount:
                result[key] = amount
                limit_left -= amount * info[key]['weight']
    FED_KZ = ('golden coin', 'silver coin', 'ruby')
    return ['{}: {}'.format(metal, int(result[metal])) for metal in FED_KZ if metal in result]

if __name__ == '__main__':
    print(treasures(
        {"silver coin": {"price": 10, "amount": 100, "weight": 10}, "ruby": {"price": 1000, "amount": 5, "weight": 200},
         "golden coin": {"price": 100, "amount": 100, "weight": 10}}, 1.8))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert treasures({'golden coin':
    #                      {'price': 100, 'weight': 50, 'amount': 200},
    #                   'silver coin':
    #                      {'price': 10, 'weight': 20, 'amount': 1000},
    #                   'ruby':
    #                      {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
    #                       'golden coin: 92', 'ruby: 2']
    # assert treasures({'golden coin':
    #                      {'price': 100, 'weight': 50, 'amount': 100},
    #                   'silver coin':
    #                      {'price': 10, 'weight': 20, 'amount': 100},
    #                   'ruby':
    #                      {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
    #                       'golden coin: 100', 'silver coin: 100', 'ruby: 1']
    # print("Coding complete? Click 'Check' to earn cool rewards!")
