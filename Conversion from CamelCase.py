def from_camel_case(name):
    return ''.join(['_{}'.format(char.lower()) if char.isupper() else char for char in name]).strip('_')