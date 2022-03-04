# Already solved swap.py where all elements of the list have to be swap cased and
# the last two integers if exist in the string must swap positions
def ShiftLet(take):
    take, swaptake = list(take), []
    for i in take:
        swaptake.append(i.upper() if i == i.lower() else i.lower())
    inds = [i for i, data in enumerate(swaptake) if data.isnumeric()]
    return Cat(''.join(swaptake), inds)

def Cat(swap, ind):
    res = swap[:ind[-2]] + str(swap[ind[-1]]) + swap[ind[-2]+1:ind[-1]] + str(swap[ind[-2]]) + swap[ind[-1]+1:]
    print(res)

ShiftLet(str(input()))