#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    hash_map = dict()
    for i in magazine:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    for i in note:
        if i not in hash_map or hash_map[i] == 0:
            return "No"
        else:
            hash_map[i] -= 1
    return "Yes"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))