from math import e, log, exp

def lambertW(x, prec=0.0001):
    w = 0
    w_min = w * exp(w)
    w_max = (w + 1) * exp(w)

    while prec < abs((x-w_min)/w_max):
        w -= (w_min-x)/(w_max-(w+2)*(w_min-x)/(2*w+2))
        if (prec > abs((x-w_min)/w_max)):
            break
        w_min = w*exp(w)
        w_max = (w+1)*exp(w)
    return w

def super_root(number):
    return e ** lambertW(log(number, e))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
