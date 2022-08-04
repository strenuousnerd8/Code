#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter
def isValid(s):
    # Write your code here
    count = dict()

    for i in s:
        count[i] = count.get(i, 0) + 1

    if len(set(count.values())) == 1:
        return "YES"

    elif len(set(count.values())) > 2:
        return "NO"

    else:
        for i in count:
            count[i] -= 1
            temp = list(count.values())
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return "YES"
            else:
                count[i] += 1
        return "NO"

if __name__ == '__main__':
    result = isValid(input())
    print(result)
