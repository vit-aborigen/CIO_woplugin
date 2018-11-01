def checkio(data):
    binary_list = [''.join([bin(int(digit))[2:].zfill(8) for digit in adress.split('.')]) for adress in data]
    compared = [all(bit == bits[0] for bit in bits) for bits in zip(*binary_list)]
    first_diff_position = compared.index(False)
    ip_binary = binary_list[0][:first_diff_position]
    ip = list(map(lambda x: int (x, 2), [ip_binary[i:i + 8].ljust(8, '0') for i in range(0, first_diff_position, 8)]))
    while len(ip) < 4:
        ip += 0,
    ip += first_diff_position,
    return ('{}.{}.{}.{}/{}'.format(*ip))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
