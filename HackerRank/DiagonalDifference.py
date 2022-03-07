

def diagonalDifference(arr):
    # Write your code here
    lrsum = 0
    rlsum = 0
    for i, data in enumerate(arr):
      try:
        lrsum = data[i] + arr[i+1][i+1]
        rlsum = data[i+1] + arr[i-1][i]
      except IndexError:
        pass
    return rlsum - lrsum

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
