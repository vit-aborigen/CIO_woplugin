def house(plan):
    if '#' not in plan: return 0
    top, bottom, left, right = 1000, -1, 1000, -1

    for idx, line in enumerate(plan[1:].splitlines()):
        if '#' in line:
            top = min(top, idx)
            bottom = max(bottom, idx)
            left = min(left, line.find('#'))
            right = max(right, line.rfind('#'))
    return (bottom - top + 1) * (right - left + 1)



if __name__ == '__main__':

    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24
#
#     assert house('''0000000000
# #000##000#
# ##########
# ##000000##
# 0000000000
# ''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
