#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    f = []
    while len(s) > 0:
        f.append(s.count(s[0]))
        s = s.replace(s[0],'')
    n = min(f)
    x = max(f)
    if x == n or (f.count(n) == len(f)-1 and x-n == 1) or (f.count(x) == len(f)-1 and n == 1):
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    result = isValid(input())
    print(result)
