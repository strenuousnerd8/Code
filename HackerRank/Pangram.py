# A pangram is a string that contains every letter of the alphabet.
# Given a sentence determine whether it is a pangram in the English alphabet.
# Ignore case. Return either pangram or not pangram as appropriate.
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = list(s.lower())
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    if all(elem in s for elem in alphabets):
      return 'pangram'
    else:
      return 'not pangram'

if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result + '\n')