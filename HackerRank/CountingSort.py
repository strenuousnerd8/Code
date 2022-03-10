# The counting sort, does not require comparison.
# Instead, you create an integer array whose index range covers the entire range of values in your array to sort.
# Each time a value occurs in the original array, you increment the counter at that index. At the end,
# run through your counting array, printing the value of each non-zero valued index that number of times.
#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    sol = [0] * 100
    for i in [int(n) for n in arr]:
        sol[i] += 1
    return sol

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
    print('\n')