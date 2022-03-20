#Main Program
def rotateIt(k, lis):
    return ' '.join(lis[-int(k):] + lis[:int(k)+1])

#Driver Code
t = int(input())
for i in range(t):
    n, k = input().split()
    lis = str(input()).split()
    print(rotateIt(k, lis))