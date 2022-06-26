# Rotate an array 'arr' of size 'n' by 'k' positions

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(' '.join(map(str, arr[-k:] + arr[0:-k])))