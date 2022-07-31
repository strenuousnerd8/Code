#med 6 large 8
def solve(N):
    if N % 2 != 0 or N < 6:
        return -1
    count = 0
    medium = N
    while medium > 0:
        medium -= 6
        count += 1
    medium = count
    large = N
    count = 0
    while large > 0:
        large -= 8
        count += 1
    large = count
    return min(medium, large)

if __name__ == '__main__':
    print('\n')
    N = int(input().strip())
    outcome = solve(N)
    print(str(outcome) + '\n')