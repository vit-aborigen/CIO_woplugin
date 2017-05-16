def checkio(n, m):
    n_str = bin(n)[2:].rjust(25, '0')
    m_str = bin(m)[2:].rjust(25, '0')
    counter = 0
    for i in range(len(n_str)):
        if n_str[i] != m_str[i]:
            counter += 1

    return counter