#input hEY3 a7yY5O, wHa3t f8as9O
def ShiftLet(take):
    resultant = ""
    for i in take:
        if i == i.upper():
            i = i.lower()
            resultant += i
        elif i == i.lower():
            i = i.upper()
            resultant += i
        else:
            resultant += i
    for i in range(len(resultant)-1, len(resultant) // 2, -1):
        storeA, indexA = 0, 0
        if resultant[i].isnumeric():
            storeA = resultant[i]
            indexA = resultant.index(resultant[i])
            break
    for j in range(len(resultant)-1, len(resultant) // 2, -1):
        storeB, indexB = 0, 0
        if resultant[j].isnumeric():
            storeB = resultant[j]
            indexB= resultant.index(resultant[j])
    resultant = resultant[:indexB] + storeA + resultant[indexB+1:indexA] + storeB + resultant[indexA+1:]
    return resultant

print(ShiftLet(str(input())))