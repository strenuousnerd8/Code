

def diagonalDifference(arr):
    # Write your code here
    lrsum = rlsum = 0
    for i in range(len(arr[0])):
      lrsum += arr[i][i]
      rlsum += arr[i][-i-1]
    return abs(lrsum - rlsum)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
