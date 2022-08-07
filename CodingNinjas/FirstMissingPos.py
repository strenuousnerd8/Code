def firstMissing(arr, n):
    # Write your function here.
    arr = [i for i in arr if i > 0]
    if arr == []:
        return 1
    wide = range(1, n + 1)
    arr.sort()
    for i in range(len(arr)):
        if wide[i] != arr[i]:
            return wide[i]
    return arr[-1] + 1


# Main Code
t=int(input())

for j in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    ans = firstMissing(arr,n)

    print(ans)
