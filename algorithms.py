alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(body):
    inverted = body.frase[::-1]
    a = body.a
    b = body.b
    encrypted = ''
    flag = 1
    for i in inverted:
        if flag % 2 != 0:
            actual_position = alphabet.index(i)
            new_position = actual_position + a
            if new_position > 27:
                new_position = new_position - 27
            encrypted = encrypted + alphabet[new_position]
        else:
            actual_position = alphabet.index(i)
            new_position = actual_position + b
            if new_position > 27:
                new_position = new_position - 27
            encrypted = encrypted + alphabet[new_position]
        flag += 1
    return encrypted

def decrypt(body):
    frase = body.frase
    a = body.a
    b = body.b
    decrypted = ''
    flag = 1
    for i in frase:
        if flag % 2 != 0:
            actual_position = alphabet.index(i)
            new_position = actual_position - a
            decrypted = decrypted + alphabet[new_position]
        else:
            actual_position = alphabet.index(i)
            new_position = actual_position - b
            decrypted = decrypted + alphabet[new_position]
        flag += 1
    return decrypted[::-1]