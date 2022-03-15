
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)]
    lastAnswer = 0
    res = []
    for i in queries:
        if i[0] == 1:
            idx = (i[1] ^ lastAnswer) % n
            arr[idx].append(i[2])
        else:
            idx = (i[1] ^ lastAnswer) % n
            lastAnswer = arr[idx][i[2] % len(arr[idx])]
            res.append(lastAnswer)
    return res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)