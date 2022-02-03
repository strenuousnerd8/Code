def findDividedString(str):
    if(len(str) % 2 == 0):
        print(str[0:len(str)-1:2])
    elif(len(str) % 2 != 0):
        print(str[0:len(str)-1:3])

findDividedString("heyheyhey")
findDividedString("heyhi")
findDividedString("hey")