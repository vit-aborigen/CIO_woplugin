def simplify_path(path):
    start_with_slash = path.startswith('/')
    new_path = []
    for folder in path.split('/'):
        if folder == '..':
            if new_path and new_path[-1] != '..':
                new_path.pop()
            elif not start_with_slash:
                new_path.append('..')
        elif folder == '.':
            continue
        elif folder:
            new_path.append(folder)

    if start_with_slash:
        return '/' + '/'.join(new_path)
    if not new_path:
        return '.'
    return '/'.join(new_path)

print(simplify_path('.././..'))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # last slash is not important
    assert simplify_path('/a/') == '/a'

    # double slash can be united in one
    assert simplify_path('/a//b/c') == '/a/b/c'

    # double dot - go to previous folder
    assert simplify_path('dir/fol/../no') == 'dir/no'
    assert simplify_path('dir/fol/../../no') == 'no'

    # one dot means current dir
    assert simplify_path('/a/b/./ci') == '/a/b/ci'
    assert simplify_path('vi/..') == '.'
    assert simplify_path('./.') == '.'

    # you can't go deeper than root folder
    assert simplify_path('/for/../..') == '/'
    assert simplify_path('/for/../../no/..') == '/'

    # not all double-dots can be simplyfied in related path
    assert simplify_path('for/../..') == '..'
    assert simplify_path('../foo') == '../foo'

    print('Simply enough! Let\'s check it now!!')