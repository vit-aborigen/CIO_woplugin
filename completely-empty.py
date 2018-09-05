import collections.abc as cabc

def isEmpty(element):
    if isinstance(element, dict):
        return (not element) or ('' in element and len(element) == 1)
    elif isinstance(element,(int, float)):
        return False
    elif isinstance(element, (list, tuple)):
        return completely_empty(element)
    elif hasattr(element, '__iter__'):
        if isinstance(element, (str, cabc.Iterator)):
            return not bool(len(list(element)))
        return False
    elif element is None:
        return False

    return not bool(len(element))

def completely_empty(val):
    result = []
    for element in val:
        result.append(isEmpty(element))
    return all(result)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    assert completely_empty([iter(())]) == True
    assert completely_empty([type('', (), {'__iter__': None})()]) == False
