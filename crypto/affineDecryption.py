from Cryptodome.Util.number import inverse
from string import ascii_lowercase as alphabet

alphabet = alphabet + "æøå"
au = alphabet.upper()


def decrypt(string, a, b):
    plaintext = ''
    ai = inverse(a, len(alphabet))
    for char in string:
        if char in alphabet:
            plaintext += alphabet[(ai*(alphabet.index(char) - b)) %
                                  len(alphabet)]
        elif char in au:
            plaintext += au[(ai*(au.index(char) - b)) % len(au)]
        else:
            plaintext += char
    return plaintext


cipherText = 'SQFPNB{Uznnz xfd zm bqm pqwlzd, hzm qææz ia iqææzd...}'

for a in range(0, 10):
    for b in range(0, 10):
        plaintext = decrypt(cipherText, a, b)
        if plaintext.startswith('UIACTF'):
            print(plaintext)
