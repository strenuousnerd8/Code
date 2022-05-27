def printHanoi(pegs):
    height = sum(map(len,pegs))
    for r in reversed(range(height)):
        for peg in pegs:
            disc = "-" * (0 if r>=len(peg) else peg[r])
            print(f"{disc:>{height}}|{disc:{height}}", end=" ")
        print()
    invalid = any(p[::-1]!=sorted(p) for p in pegs)
    print("="*(height*6+5),"INVALID"*invalid)
    print()

def moveHanoi(pegs,fromPeg,toPeg):
    pegs[toPeg].append(pegs[fromPeg].pop(-1))
    printHanoi(pegs)

def solveHanoi(count,fromPeg=0,toPeg=2,tempPeg=1):
    if not count: return
    yield from solveHanoi(count-1,fromPeg,tempPeg,toPeg)
    yield fromPeg,toPeg
    yield from solveHanoi(count-1,tempPeg,toPeg,fromPeg)

pegs = [[3,2,1],[],[]]
printHanoi(pegs)
for f,t in solveHanoi(3):
    moveHanoi(pegs,f,t)