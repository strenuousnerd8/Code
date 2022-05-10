n = int(input())
arr1 = list(map(int, list(input().split())))
m = int(input())
arr2 = list(map(int, list(input().split())))
res = arr1 + arr2
res.sort()
res = [str(i) for i in res]
print(' '.join(res[:len(arr1)]))
print(' '.join(res[len(arr1):]))