def minimumBribes(n, q):
    # Write your code here
    comp = list(range(1, n+1))
    print(comp, q, sep="\n")
    changed = []
    for i in range(n):
        if comp[i] != q[i]:
            changed.append(q[i])

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(n, q)