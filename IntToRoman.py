# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
def convertToRoman(num):
    resultant = num
    Roman = []
    while resultant != 0:
        if resultant >= 1000:
            Roman.append("M")
            resultant -= 1000
        elif resultant >= 500:
            Roman.append("D")
            resultant -= 500
        elif resultant >= 100:
            Roman.append("C")
            resultant -= 100
        elif resultant == 90:
            Roman.append("XC")
            resultant -= 90
        elif resultant >= 50:
            Roman.append("L")
            resultant -= 50
        elif resultant == 40:
            Roman.append("XL")
            resultant -= 40
        elif resultant >= 10:
            Roman.append("X")
            resultant -= 10
        elif resultant == 9:
            Roman.append("IX")
        elif resultant >= 5:
            Roman.append("V")
            resultant -= 5
        elif resultant >= 1:
            Roman.append("I")
            resultant -= 1
    return Roman

print(''.join(convertToRoman(int(input()))))