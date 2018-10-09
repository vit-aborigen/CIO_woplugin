def merge_painted(list_1, list_2):
    """
    :param list_1: list of lists - represents already painted part of wall
    :param list_2: list - part of wall that should be merged with already painted wall
    :return: list of lists - painted part updated
    """
    updated =  sorted((list_1 + [list_2]), key=lambda x: x[0])
    result = [updated[0]]

    for interval in updated:
        if interval[0] > result[-1][1] + 1:
            result.append(interval)
        else:
            result[-1][1] = max(interval[1], result[-1][1])
    return result


def len_painted(painted_part):
    return sum([(interval[1] - interval[0] + 1) for interval in painted_part])


def checkio(required, operations):
    painted_part = [operations[0]]
    step = 0

    for operation in operations:
        painted_part = merge_painted(painted_part, operation)
        step += 1
        if len_painted(painted_part) >= required:
            return step
    return -1


if __name__ == '__main__':
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
    assert checkio(20,[[1,2],[20,30],[25,28],[5,10],[4,21],[1,6]]) == 5