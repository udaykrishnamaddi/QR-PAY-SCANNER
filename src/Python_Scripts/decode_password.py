decryptDictionary = {

    '$': 0, 'C': 1, '>': 2, 'Y': 3, 'V': 4, '<': 5, 'D': 6, '(': 7, ')': 8, 'O': 9, 'P': 10,
    ',': 11, '-': 12, 'B': 13, 'I': 14, 'J': 15, 'K': 16, 'L': 17, 'G': 18, 'M': 19, ']': 20,
    '?': 21, 'S': 22, '[': 23, '}': 24, 'U': 25, '{': 26, 'H': 27, 'a': 28, 'b': 29, 'c': 30,
    'd': 31, 'e': 32, 'f': 33, 'g': 34, 'h': 35, '@': 36, 'j': 37, 'k': 38, 'l': 39, 'm': 40,
    'n': 41, '&': 42, 'p': 43, 'q': 44, 'r': 45, 's': 46, 't': 47, 'u': 48, 'v': 49, 'w': 50,
    'x': 51, 'y': 52, 'z': 53, 'A': 54

}


def decryptPassword(encryptedPassword):

    list_password = []

    for ch in encryptedPassword:

        list_password.append(decryptDictionary[ch])

    for i in range(5, -1, -1):

        if i!=0:
            list_password[i] = list_password[i] - list_password[i-1]

    list_password.reverse()

    decryptedPassword = ''

    for i in list_password:

        decryptedPassword += str(i)

    return decryptedPassword