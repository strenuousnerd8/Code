import math as m
def maxSubsetSum(k):
    # Complete this function
    result = []
    for n in k:
        res = 1
        for i in range(2, int(m.sqrt(n) + 1)):

            curr_sum = 1
            curr_term = 1

            while n % i == 0:

                n = n / i;

                curr_term = curr_term * i;
                curr_sum += curr_term;

            res = res * curr_sum

        if n >= 2:
            res = res * (1 + n)

        result.append(int(res))
    return result


if __name__ == "__main__":
    size = int(input().strip())
    k = []
    k_i = 0
    for k_i in range(size):
        k_t = int(input().strip())
        k.append(k_t)
    res = maxSubsetSum(k)
    print("\n".join(map(str, res)))