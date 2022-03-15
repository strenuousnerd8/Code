#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    # Solution 1 (Time inefficient)
    # return 'YES' if [True for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:])] else 'NO'
    # Solution 2 (Time Efficient)
    rp = sum(arr)
    lp = 0
    for i in arr:
        rp-=i
        if lp == rp:
            return 'YES'
        lp+=i
    return 'NO'

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)
