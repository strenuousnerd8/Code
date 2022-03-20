# find combinations of DNA sequences
nodna = int(input())
samples = str(input()).split()
divisions = int(input())
samples = str(input()).split()
divisions = int(input())
resultdna = [''.join(samples[i:i+divisions]) for i in range(0, len(samples), divisions)]
print(resultdna)

# Number of ommitted special characters
NAME = list(str(input()))
omit = []
for x in NAME:
    if x.isalpha():
        omit.append(x)
    elif x.isnumeric():
        omit.append(x)
    elif x == " ":
        omit.append(x)

print(len(NAME) - len(omit))

# kth smallest number
n = int(input())
lis = str(input()).split()
neg = int(input())
lis = [int(x) for x in lis]
for x in range(neg-1):
    lis.remove(min(lis))
print(min(lis))

# split in pairs and remove smallest, keep singles
stre = list(str(input()))
increasing_slices = 0
sliced = []
result = []
for i in range(len(stre)):
    increasing_slices += 2
    sliced.append("".join(stre[increasing_slices-2:increasing_slices]))

for j in sliced:
    if len(j) == 1 and j.isnumeric():
        result.append(j)
    elif len(j) == 2:
        if j[0] > j[1]:
            result.append(j[0])
        elif j[1] > j[0]:
            result.append(j[1])
        elif j[1] == j[0]:
            result.append(j[1])

print(''.join(result))