from Cryptodome.Util.number import inverse
from string import ascii_lowercase as alphabet

alphabet = alphabet + "æøå"
au = alphabet.upper()


def decrypt(string, a, b):
    pt = ''
    ai = inverse(a, len(alphabet))
    for char in string:
        if char in alphabet:
            pt += alphabet[(ai*(alphabet.index(char) - b)) % len(alphabet)]
        elif char in au:
            pt += au[(ai*(au.index(char) - b)) % len(au)]
        else:
            pt += char
    return pt


cipherText = 'SQFPNB{Uznnz xfd zm bqm pqwlzd, hzm qææz ia iqææzd...}'

for a in range(0, 10):
    for b in range(0, 10):
        pt = decrypt(cipherText, a, b)
        if pt.startswith('UIACTF'):
            print(pt)
