from collections import deque

def checkio(data):
    word_1, finish = map(deque, data.split('-'))
    word_2, buffer, result = deque(), deque(), []
    while finish:
        counter = 0
        letter = finish.popleft()
        while word_1[-1] != letter:
            word_2.append(word_1.pop())
            result += '12',
            counter += 1
        buffer.append(word_1.pop())
        result += '10',
        while counter:
            word_1.append(word_2.pop())
            result += '21',
            counter -= 1
        word_2.append(buffer.pop())
        result += '02',
        print(result, word_2)




print(checkio("rice-cire"))
"10,12,12,12,02"


# if __name__ == '__main__':
#     #This part is using only for self-checking and not necessary for auto-testing
#     GOOD_ACTIONS = ("12", "10", "01", "02", "20", "21")
#
#     def check_solution(func, anagrams, min_length):
#         start, end = anagrams.split("-")
#         stacks = [[], list(start), []]
#         user_result = func(anagrams)
#         actions = user_result.split(",")
#         user_actions = []
#         for act in actions:
#             if act not in GOOD_ACTIONS:
#                 print("Wrong action")
#                 return False
#             from_s = int(act[0])
#             to_s = int(act[1])
#             if not stacks[from_s]:
#                 print("You can not get from an empty stack")
#                 return False
#             if to_s == 0 and stacks[to_s]:
#                 print("You can not push in the full buffer")
#                 return False
#             stacks[to_s].append(stacks[from_s].pop())
#             user_actions.append(act)
#         res_word = ''.join(stacks[2])
#         if len(actions) > min_length:
#             print("It can be shorter.")
#             return False
#         if res_word == end:
#             return True
#         else:
#             print("The result anagram is wrong.")
#             return False
#
#     assert check_solution(checkio, "rice-cire", 5), "rice-cire"
#     assert check_solution(checkio, "tort-trot", 4), "tort-trot"
#     assert check_solution(checkio, "hello-holle", 14), "hello-holle"
#     assert check_solution(checkio, "anagram-mragana", 8), "anagram-mragana"
#     assert check_solution(checkio, "mirror-mirorr", 25), "mirror-mirorr"
