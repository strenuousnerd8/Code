import string
plainText = str(input("Enter your Plain Text:\t")).lower().strip()
k, cipherText, rollingKey = int(input("Enter your Key:\t")), [], 0
library = string.ascii_lowercase.replace('', ' ').split()
choice = str(input("Type X to encrypt and Y to Decrypt:\t"))
if choice.lower() == 'y':
    k = 26 - k
for i in plainText:
    if i.isalpha():
        if k < 0:
            rollingKey = library.index(i) - k
        else:
            rollingKey = library.index(i) + k
        if rollingKey > 25:
            rollingKey -= 26
        cipherText.append(library[rollingKey])
    else:
        cipherText.append(' ')
print("Cipher Text:\t" + ''.join(cipherText))