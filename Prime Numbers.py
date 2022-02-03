#Let's only print Palindromic Primes
def findPrimePalins(n):
    start = 100
    for i in range(start, n+1):
        if i > 1:
            for x in range(2, i):
                if i % x != 0:
                    palin = str(i)[::-1]
                    if str(i) == palin:
                        print(palin, end=', ')
                    break

getRange = int(input("Enter your range for palindromic primes:\t"))
findPrimePalins(getRange)