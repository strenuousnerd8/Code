# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
# Solution time complexity: O(n)

def sockMerchant(n, ar):
    # Write your code here
    temp = []
    lis = []
    res = 0
    for i in ar:
        if ar.count(i) >= 2 and i not in temp:
          temp.append(i)
          lis.append(ar.count(i))
    for i in lis:
      if i % 2 == 0:
        res += (i / 2)
      else:
        res += ((i - 1) / 2)
    return int(res)

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')
