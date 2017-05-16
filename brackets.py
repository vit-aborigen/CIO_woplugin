def checkio(expression):
    brackets = ""
    dictionary = "([{)]}"
    for char in expression:
        if char in dictionary:
            brackets += char
    if len(brackets) == 0:
        return True

    opened = [] #stack of opened brackets
    for bracket in brackets:
        if bracket in dictionary[0:3]:
            opened += bracket,
        elif (len(opened) == 0): #stack is empty
            return False
        else:
            if bracket != dictionary[dictionary.index(opened[-1])+3]:
                return False
            opened.pop()

    return len(opened) == 0
