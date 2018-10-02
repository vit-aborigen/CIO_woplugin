def from_camel_case(name):
    return ''.join(['_{}'.format(char.lower()) if char.isupper() else char for char in name]).strip('_')

if __name__ == '__main__':
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")