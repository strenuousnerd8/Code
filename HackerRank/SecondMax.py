#Print the runner up of the sports event
n = int(input())
arr = list(map(int, str(input()).split()))
print(max(list(filter((max(arr)).__ne__, arr))))
