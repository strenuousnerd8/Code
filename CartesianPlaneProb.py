def solve(N, U, D, I, R):
    total = 0
    if N <= 1:
       total = total + (U + I + D + R)
    else:
        total = (total + U + I + D + R) - 0.25
    return "{0:0.9f}".format(total)

if __name__ == '__main__':
    N = int(input())
    U = float(input())
    D = float(input())
    I = float(input())
    R = float(input())
    outcome = solve(N, U, D, I, R)
    print(str(outcome) + '\n')