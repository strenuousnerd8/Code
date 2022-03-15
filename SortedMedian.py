#Find median of a sorted list

def findMedian(arr):

    return sorted(arr)[len(arr)//2]

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(str(result) + '\n')

