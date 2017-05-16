def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    sign = '' if number >= 0 else '-'
    number = abs(number)
    i = 0

    while i < (len(powers)-1) and (number / base ** (i+1) >= 1):
        i += 1
    number /= base ** i

    if decimals:
        number = ('{:.' + str(decimals) + 'f}').format(round(number, decimals))
    else:
        number = int(number)
    return sign + str(number) + powers[i] + suffix

friendly_number(255000000000, powers=["","k","M"])
#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(12000000, decimals=3) == '12.000M', '12.000M'
    assert friendly_number(255000000000, powers=["","k","M"]) == '255000M', 'last'



