from copy import deepcopy

COLORS = ['blue', 'green', 'red', 'white', 'yellow']
PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
NUMBERS = ['1', '2', '3', '4', '5']
QUESTIONS = ["color",  "pet", "beverage", "cigarettes", "nationality", "number"]
COMBINED = [COLORS, PETS, BEVERAGES, CIGARETTES, NATIONALITY]

def find_property(name):
    for values in COMBINED:
        if name in values:
            return COMBINED.index(values)

def find_empty_values(idx, row):
    all_values = set(COMBINED[idx])
    row_values = set(row)
    return ((all_values - row_values).pop(), row.index('_'))

def find_value_in_matrix(value, matrix):
    for idx, row in enumerate(matrix):
        if value in row:
            return (idx, row.index(value))
    return (-1, -1)

def update_matrix(matrix):
    updated = False
    for idx, row in enumerate(matrix):
        if sum([1 for value in row if value == '_']) == 1:
            value, position = find_empty_values(idx, row)
            row[position] = value
            updated = True
    return updated

def answer(relations, question):
    initial_information = deepcopy(relations)
    not_yet_used_information = list(relations)
    matrix = [['_' for i in range(5)] for j in range(5)]

    for pair in initial_information:
        a,b = pair.split('-')
        if a.isdigit():
            matrix[find_property(b)][int(a)-1] = b
            if pair in not_yet_used_information:
                not_yet_used_information.remove(pair)
        if b.isdigit():
            matrix[find_property(a)][int(b)-1] = a
            if pair in not_yet_used_information:
                not_yet_used_information.remove(pair)

    at_least_one_value_was_used = True
    while not_yet_used_information:
        initial_information = deepcopy(not_yet_used_information)

        if not at_least_one_value_was_used:
            if not update_matrix(matrix):
                return 'Can not be solved'

        at_least_one_value_was_used = False

        for pair in initial_information:
            a, b = pair.split('-')
            a1, a2 = find_value_in_matrix(a, matrix)
            if a1 != -1:
                matrix[find_property(b)][a2] = b
                at_least_one_value_was_used = True
                if pair in not_yet_used_information:
                    not_yet_used_information.remove(pair)

            b1, b2 = find_value_in_matrix(b, matrix)
            if b1 != -1:
                matrix[find_property(a)][b2] = a
                at_least_one_value_was_used = True
                if pair in not_yet_used_information:
                    not_yet_used_information.remove(pair)

    update_matrix(matrix)

    value, quest = question.split('-')
    j = find_value_in_matrix(value, matrix)[1]
    i = QUESTIONS.index(quest)
    if i > 4:
        return str(j + 1)
    return matrix[i][j]


def show_matrix(matrix):
    # used just for convenient matrix representation
    values = ['COLOR', 'PETS', 'BEVERAGES', 'CIGARETTES', 'NATIONALITY']
    header = ['\nHouse number'] + [str(i+1) for i in range(5)]
    print('{:^12}   {:^12}   {:^12}   {:^12}   {:^12}   {:^12}'.format(*header))
    for row in zip(values, matrix):
        print('{:<12}   {:^12}   {:^12}   {:^12}   {:^12}   {:^12}'.format(row[0], *row[1]))



if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?
