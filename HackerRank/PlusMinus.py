# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with places after the decimal.
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    poscount = negcount = zero = 0
    for x in arr:
        if x > 0:
            poscount += 1
        elif x < 0:
            negcount += 1
        else:
            zero += 1
    print("{:.6f}".format(poscount / len(arr)))
    print("{:.6f}".format(negcount / len(arr)))
    print("{:.6f}".format(zero / len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
