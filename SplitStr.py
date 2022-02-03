def splitStr(x):
    alpha = ""
    special = ""
    num = 0
    for i in x:
        if str(i).isalpha():
            alpha += i
        elif str(i).isnumeric():
            num += int(i)
        else:
            special += i
    print(alpha + " " + special + " " + str(num))

x = str(input()).lower().replace(' ', '')
splitStr(x)