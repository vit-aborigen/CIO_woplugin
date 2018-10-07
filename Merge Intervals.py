def merge_intervals(intervals):
    if not len(intervals): return []
    current = list(intervals[0])
    result = []

    for interval in intervals[1:]:
        if interval[1] <= current[1]:
            continue
        elif interval[0] <= current[1] + 1:
            current[1] = interval[1]
        else:
            result.append(tuple(current))
            current = interval
    result.append(tuple(current))
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')