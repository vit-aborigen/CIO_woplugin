DIGITS = [
    0b1111110, # 0
    0b0110000, # 1
    0b1101101, # 2
    0b1111001, # 3
    0b0110011, # 4
    0b1011011, # 5
    0b1011111, # 6
    0b1110000, # 7
    0b1111111, # 8
    0b1111011, # 9
]

LITERALS = 'GFEDCBA'

def literal_to_binary(literal):
    # get literal index -> convert to 7-signs binary -> convert to int (same format as items in DIGITS list)
    return int(bin(1 << LITERALS.index(literal))[2:], 2)

def convert_pair_to_binary(segments_set):
    digit_first, digit_second = 0, 0
    for segment in segments_set:
        if segment in LITERALS:
            digit_first += literal_to_binary(segment)
        else:
            digit_second += literal_to_binary(segment.upper())
    return (digit_first, digit_second)

def compare_mask(lit, broken):
    mask = lit | broken
    return sum([1 for digit in DIGITS if (digit & mask == digit) and (digit & lit == lit)])

def seven_segment(lit_seg, broken_seg):
    lit_first, lit_second = convert_pair_to_binary(lit_seg)
    broken_first, broken_second = convert_pair_to_binary(broken_seg)
    return compare_mask(lit_first, broken_first) * compare_mask(lit_second, broken_second)


if __name__ == '__main__':
    print(seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}))
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')