# Optimized CaesarCipher code using formula, very readable.
# Encryption E(p) = (p + k) mod 26
# Decryption D(c) = (c - k) mod 26
import string
library, res = string.ascii_lowercase, []
userText, k = str(input("Enter plain/cipher text :\t")), int(input("Enter Key :\t"))
choice = True if input("Press E for encryption or D for decryption :\t").lower() == 'e' else False
for letter in userText:
    if letter not in library:
        res.append(letter)
    else:
        if choice:
            res.append(library[(library.index(letter) + k) % 26])
        else:
            res.append(library[(library.index(letter) - k) % 26])
print(''.join(res).upper())
