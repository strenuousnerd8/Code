import math
import itertools
def encryption(s):
    # Write your code here
    b = math.ceil(math.sqrt(len(s)))
    res = [s[i : b + i] for i in range(0, len(s), b)]
    encrypt = [''.join(list(i)) for i in itertools.zip_longest(*res, fillvalue='')]
    return ' '.join(encrypt)

    # Alternate solution using expression slicing
    # c = math.ceil(math.sqrt(len(s) - s.count(" ")))
    # for i in range(c):
    #     print(s.replace(" ", "")[i::c])

if __name__ == '__main__':

    s = "feedthedog"

    result = encryption(s)

    print(result)