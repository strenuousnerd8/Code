# Find prime numbers in an interval
def findPrimes(s, e):
    primes = []
    for i in range(s, e):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return primes


# Driver code

print(*findPrimes(2, 7), sep=" ")
