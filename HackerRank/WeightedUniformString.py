#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#
import string

def weightedUniformStrings(s, queries):
    # Write your code here
    eng = string.ascii_lowercase
    hash_map = dict()
    for i, value in enumerate(eng):
            hash_map[value] = i + 1
    scores = set()
    ctr = 1
    for i in range(len(s)):
        score = hash_map[s[i]]
        ctr = ctr + 1 if (i + 1 != len(s) and s[i + 1] == s[i]) else 1
        scores.add(score * ctr)
    res = ["Yes" if _ in scores else "No" for _ in queries]
    return res


if __name__ == '__main__':

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    print(result)
