def is_family(tree):
    used_names = []
    current_fathers = []
    current_sons = []
    for tier in tree:
        if tier[1] in current_fathers or tier[1] in used_names: return False
        if tier[0] in used_names: return False
        if tier[0] not in current_fathers:
            used_names = current_fathers[:] if len(current_fathers) else []
            if tier[0] not in current_sons and len(current_sons): return False
            current_fathers = current_sons[:] if len(current_sons) else tier[0]
            if tier[1] in current_fathers or tier[1] in used_names: return False
            current_sons = tier[1],
        else:
            current_sons += tier[1],
    return True

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike'],
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
