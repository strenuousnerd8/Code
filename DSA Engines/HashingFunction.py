Towns = ['Nashville', 'OldTown', 'St Pedrosa', 'Willesburg']
hashLen = 5
hash = [[] for _ in range(hashLen)]

def hashFunc(s):
    res = sum(ord(i) for i in s) % hashLen
    return res

for i in Towns:
    hash[hashFunc(i)].append(i)

print(hash)
