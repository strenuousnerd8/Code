def goodnessOfString(s):
    # Write your code here.
    dep = 0
    res = 0
    tes = ""
    for i in s:
        if i == '[':
            dep += 1
        elif i.isnumeric():
            tes += i
        elif i == ',':
            if tes != "":
                res += (int(tes) * dep)
            tes = ""
        elif i == ']':
            if tes != "":
                res += (int(tes) * dep)
            tes = ""
            dep -= 1
    return res

s = "[1,[2,3],[4,[5,6]]]"
print(goodnessOfString(s))