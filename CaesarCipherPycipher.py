from pycipher import Caesar
userText, k = str(input("Enter plain/cipher text :\t")), int(input("Enter Key :\t"))
choice = True if input("Press E for encryption or D for decryption :\t").lower() == 'e' else False
if choice:
    print(Caesar(key=k).encipher(userText))
else:
    print(Caesar(key=k).decipher(userText))