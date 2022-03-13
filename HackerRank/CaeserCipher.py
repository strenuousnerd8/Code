#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
import string

def caesarCipher(s, k):
    # Write your code here
    alphaCap = string.ascii_uppercase
    alphaLow = string.ascii_lowercase
    cipherText = []
    for character in s:
        if character.isalpha():
            if character == character.upper():
                cipherText.append(alphaCap[(alphaCap.index(character) + k) % 26])
            else:
                cipherText.append(alphaLow[(alphaLow.index(character) + k) % 26])
        else:
            cipherText.append(character)
    return ''.join(cipherText)

if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result + '\n')
