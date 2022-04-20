#
# Complete the 'getTriangleArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER_ARRAY y
#

def getTriangleArea(x, y):
    # Write your code here
    return int(abs((0.5) * (x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))))

if __name__ == '__main__':

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    y_count = int(input().strip())

    y = []

    for _ in range(y_count):
        y_item = int(input().strip())
        y.append(y_item)

    result = getTriangleArea(x, y)

    print(str(result) + '\n')
