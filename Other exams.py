# Length of range from first occurence to last occurence of b
# if a exists in slice of both occurences of b in string S
def solve(S, A, B):
    indb = 0
    inda = 0
    reverselis = S[::-1]
    for x in range(len(reverselis)-1):
        if reverselis[x] == B:
            indb = reverselis.index(B)
    indb = len(S) - indb
    indb -= 1
    for num in range(len(S)-1):
        if S[num] == B:
            inda = S.index(S[num])
            break
    if A in S[inda:indb]:
        return len(S[inda:indb])
if __name__ == '__main__':
    S = str(input())
    A = str(input())
    B = str(input())
    print(solve(S, A, B) - 2)