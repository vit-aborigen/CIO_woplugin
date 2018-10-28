def create_intervals(data):
    if not data:
        return []
    buffer = min(data),
    result = []

    for value in sorted(data)[1:]:
        if value == buffer[-1] + 1:
            buffer += value,
        else:
            result += (buffer[0], buffer[-1]),
            buffer = value,
    if len(buffer):
        result += (buffer[0], buffer[-1]),
    return result





print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5, 12}))
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
#     assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
#     print('Almost done! The only thing left to do is to Check it!')