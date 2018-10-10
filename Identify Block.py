FIGURES = {
    "I": ({1,2,3,4}, {1,5,9,13}),
    "J": ({2,6,9,10}, {1,5,6,7}, {1,2,5,9}, {1,2,3,7}),
    "L": ({1,5,9,10}, {1,2,3,5}, {1,2,6,10}, {3,5,6,7}),
    "O": ({1,2,5,6},),
    "S": ({2,3,5,6}, {1,5,6,10}),
    "T": ({1,2,3,6}, {2,5,6,10}, {2,5,6,7}, {1,5,6,9}),
    "Z": ({1,2,6,7}, {2,5,6,9}),
}

def move_figure_to_top_left(numbers):
    while not any(number in numbers for number in {1, 2, 3, 4}):
        numbers = {(num - 4) for num in numbers}
    while not any(number in numbers for number in {1, 5, 9, 13}):
        numbers = {(num - 1) for num in numbers}
    return numbers

def identify_block(numbers):
    numbers = move_figure_to_top_left(numbers)
    for figure, form in FIGURES.items():
        if numbers in form:
            return figure
    return

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert identify_block({6,7,10,11}) == 'O', 'O'
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) == None, 'None'
