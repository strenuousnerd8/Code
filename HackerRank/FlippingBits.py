from unicodedata import decimal


def flippingBits(n):
    # Write your code here
    bina = '{:032b}'. format(n)
    deci = ''.join(['1' if i == '0' else '0' for i in bina])
    return int(deci, 2)
    # This gives O(n) efficiency, instead use return (2**32 - 1) - n for O(1) efficiency

def decimalToBinary(n):
    if n > 1:
        decimalToBinary(n//2)
    return n%2

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(str(result) + '\n')
