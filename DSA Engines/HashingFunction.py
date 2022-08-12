Towns = ['Nashville', 'OldTown', 'St Pedrosa', 'Willesburg']
hash = dict()
hashLen = 5

def hashFunc(s):
    res = sum(ord(i) for i in s) % hashLen
    return res

for i in Towns:
    if hashFunc(i) not in hash:
        hash[hashFunc(i)] = []
    hash[hashFunc(i)].append(i)

print(hash)
