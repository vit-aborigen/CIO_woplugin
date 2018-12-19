from typing import List
from collections import defaultdict

FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--",
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-",
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-",
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-",
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")

def convert_font_to_single_digits_dict(font):
    digit, digits = 0, defaultdict(list)
    for idx, line in enumerate(FONT):
        for i in range(1, len(line), 4):
            digit = (digit + 1) % 10
            digits[digit].append(line[i:i+3].replace('-', '0').replace('X', '1'))
    return digits

def split_image_on_chunks(image):
    separator = (0, 0, 0, 0, 0)
    part, parts = [], []
    for row in zip(*image):
        if row != separator:
            part.append(row)
        else:
            if part:
                tmp = []
                for row in zip(*part):
                    tmp.append(''.join([str(d) for d in row]))
                parts.append(tmp)
                part = []
    return parts

def restore_digit_from_parts(parts):
    digit, digits = [], []
    separator = ('0', '0', '0', '0', '0')
    for part in parts:
        if len(part[0]) == 1:
            if digit:
                digits.append(merge_parts(digit, separator, part))
                digit = []
            else:
                digit = part
        elif digit:
            digits.append(merge_parts(separator, digit, separator))
            digit = []
        if len(part[0]) == 3:
            digits.append(part)
        elif len(part[0]) == 2:
            digits.append(merge_parts(part, separator))
    return digits

def compare_digit_from_image_with_the_standard(digit, standard, tolerance = 1):
    for mask, value in standard.items():
        if digit == value:
            return str(mask)
        errors_count = sum([sum([1 for j in range(len(row)) if digit[i][j] != value[i][j]]) for i, row in enumerate(digit)])
        if errors_count <= tolerance:
            return str(mask)
    return -1

def merge_parts(*args):
    digit, line = [], []
    for idx in range(len(args[0])):
        for part in args:
            line.append(part[idx])
        digit.append(''.join(line))
        line = []
    return digit

def checkio(image: List[List[int]]) -> int:
    ocred = ''
    font = convert_font_to_single_digits_dict(FONT)
    parts = split_image_on_chunks(image)
    for digit in restore_digit_from_parts(parts):
        result = compare_digit_from_image_with_the_standard(digit, font)
        if result == -1:
            return 'Not found'
        ocred += result
    return int(ocred)


if __name__ == '__main__':
    print(checkio([[0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0],[0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,0],[0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0],[0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0]]))