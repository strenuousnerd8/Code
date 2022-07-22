#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    s = list(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            del s[i]
            del s[i]
            i = 0
            if len(s) == 0:
                return 'Empty String'
        else:
            i+=1
    return ''.join(s)

if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

    print(result)
