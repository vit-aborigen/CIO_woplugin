def max(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        args = args[0]
    maxi = None
    for i in args:
        if maxi == None or key(i) > key(maxi):
            maxi = i
    return maxi

def min(*args, **kwargs):
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        args = args[0]
    mini = None
    for i in args:
        if mini == None or key(i) < key(mini):
            mini = i
    return mini