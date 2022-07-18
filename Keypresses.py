# Given a set of strings match the separated keypresses where -B is backspace
l = {"c, a, r, d", "c, a, r, -B, r, d"}
res = list(l)
A = [str(i) for i in res[0] if i.isalpha()]
B = [str(i) for i in res[1] if i.isalpha()]
out = []
for i in range(len(B)):
    if B[i] != 'B':
        out.append(B[i])
    else:
        out.pop(-1)

print(A == out)