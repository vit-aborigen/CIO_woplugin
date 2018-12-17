def caps_lock(text: str) -> str:
    flag = False
    result = ''
    for i in range(len(text)):
        if text[i] == 'a':
            flag = not flag
            continue
        result += text[i] if not flag else text[i].upper()
    return result



if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
