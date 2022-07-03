# Solved in 6 lines excluding question
# Divide an array in lengths of natural number sequence
# like [1],[2,3],[4,5,6]
# And find the maximum sum in all of the sequences

arr = [0, 1, 2, 3, 4, 5]
i, pos, out = 1, 0, []
while pos < (len(arr) - i + 1):
    out.append(arr[pos : pos + i])
    pos += i
    i += 1
print(max([sum(i) for i in out]))