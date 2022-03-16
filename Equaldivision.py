# Divide a given string in N equal parts

def eqDiv(stre, n):
    return [stre[i:i+n] for i in range(0, len(stre), n)]

print(eqDiv("aaabbbccc", 3))
print(eqDiv("Hellheyahowiheri", 4))