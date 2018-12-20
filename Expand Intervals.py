from itertools import chain

def expand_intervals(items):
    return chain.from_iterable([range(a, b + 1) for a,b in items])