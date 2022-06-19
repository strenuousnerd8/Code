#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    total = []
    for i in container:
        total.append(sum(i))
    types = {}
    for i in range(len(container)):
        types[i] = []
        for j in range(len(container[0])):
            types[i].append(container[j][i])
    summation = []
    for v in types.values():
        summation.append(sum(v))
    return "Possible" if sorted(total) == sorted(summation) else "Impossible"

if __name__ == '__main__':

    q = 1

    for q_itr in range(q):
        n = 3

        container = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]

        result = organizingContainers(container)

        print(result)