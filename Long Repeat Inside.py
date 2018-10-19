from collections import defaultdict
import re

def split_on_substrings(line, window_size):
    for idx in range(len(line) - window_size + 1):
        yield line[idx:idx + window_size]

def return_longest_substring(substring, indexes):
    smthing_found = []
    if len(indexes) > 1:
        for x, y in zip(indexes[0:], indexes[1:]):
            if y - x == len(substring):
                smthing_found += x, y,
        if smthing_found:
            return substring * len(set(smthing_found))
    return ''

def repeat_inside(line):
    stats = defaultdict(int)
    for window_size in range(len(line)):
        for substring in split_on_substrings(line, window_size):
            stats[substring] += 1
    filtered = sorted([k for k, v in stats.items() if v >= 2 if k], key=len, reverse=True)

    results = []
    for substring in filtered:
        starts = [match.start() for match in re.finditer(substring, line)]
        results += return_longest_substring(substring, starts),
    if results:
        return max(results, key=len)
    return ''