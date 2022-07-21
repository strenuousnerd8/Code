#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    # Write your code here
    n = 0
    for i in A:
        if i in B:
            B.remove(i)
            n += 1
    return n + 1 if n < len(A) else n - 1

if __name__ == '__main__':

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    print(result)