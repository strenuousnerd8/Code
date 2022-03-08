# Optimized CaesarCipher code using formula in 10 lines!
# Encryption E(p) = (p + k) mod 26
# Decryption E(c) = (c - k) mod 26
import string
library, res = string.ascii_lowercase, []
userText, k, choice = str(input("Enter plain/cipher text :\t")), int(input("Enter Key :\t")), [True, False]
choice = choice[0] if input("Press E for encryption or D for decryption :\t").lower() == 'e' else choice[1]
if choice:
    for letter in userText:
        res.append(library[(library.index(letter) + k) % 26])
else:
    for letter in userText:
        res.append(library[(library.index(letter) - k) % 26])
print(''.join(res))