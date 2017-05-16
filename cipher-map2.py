def recall_password(cipher_grille, ciphered_password):
    result = ""
    for i in range(4):
        result += encode(cipher_grille, ciphered_password)
        cipher_grille = rotate(cipher_grille)
    return result

def encode(cipher_grille, ciphered_password):
    result = ""
    for i in range(4):
        for j in range(4):
            if cipher_grille[i][j] == "X":
                result += ciphered_password[i][j]
    return result

def rotate(cipher_grille):
    result = ()
    for i in range(4):
        string = ""
        for j in range(4):
            string += cipher_grille[3-j][i]
        result += string,
    return result