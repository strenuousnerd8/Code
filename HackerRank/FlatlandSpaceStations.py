# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    pass

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)