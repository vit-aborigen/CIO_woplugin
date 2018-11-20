def cut(plan):
    if '#' not in plan: return 0
    top, bottom, left, right = 1000, -1, 1000, -1

    for idx, line in enumerate(plan[1:].splitlines()):
        if '#' in line:
            top = min(top, idx)
            bottom = max(bottom, idx)
            left = min(left, line.find('#'))
            right = max(right, line.rfind('#'))
    return [line[left:right + 1] for line in plan.split()[top:bottom + 1]]

def keys_and_locks(lock, some_key):
    lock_pattern = cut(lock)
    key_pattern = cut(some_key)
    degree = 0
    while degree != 360:
        if key_pattern == lock_pattern:
            return True
        key_pattern = [''.join(value) for value in zip(*key_pattern[::-1])]
        degree += 90
    return False

if __name__ == '__main__':
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert keys_and_locks('''
# 0##0
# 0##0
# 00#0
# 00##
# 00##''',
# '''
# 00000
# 000##
# #####
# ##000
# 00000''') == True
#
#     assert keys_and_locks('''
# ###0
# 00#0''',
# '''
# 00000
# 00000
# #0000
# ###00
# 0#000
# 0#000''') == False
#
#     assert keys_and_locks('''
# 0##0
# 0#00
# 0000''',
# '''
# ##000
# #0000
# 00000
# 00000
# 00000''') == True
#
#     assert keys_and_locks('''
# ###0
# 0#00
# 0000''',
# '''
# ##00
# ##00''') == False
#
#     print("Coding complete? Click 'Check' to earn cool rewards!")
