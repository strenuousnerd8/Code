# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    v = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six",
     7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve",
     13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen",
     18 : "eighteen", 19 : "nineteen", 20 : "twenty", 21 : "twenty one", 22 : "twenty two",
     23 : "twenty three", 24 : "twenty four", 25 : "twenty five", 26 : "twenty six",
     27 : "twenty seven", 28 : "twenty eight", 29 : "twenty nine"}

    if m <= 30:
        if m == 0:
            return f"{v[h]} o' clock"
        elif m == 1:
            return f"{v[m]} minute past {v[h]}"
        elif m == 30:
            return f"half past {v[h]}"
        elif m == 15:
            return f"quarter past {v[h]}"
        else:
            return f"{v[m]} minutes past {v[h]}"
    elif m >= 30:
        if m == 45:
            return f"quarter to {v[h + 1]}"
        elif m == 59:
            return f"{v[60 - m]} minute to {v[h + 1]}"
        else:
            return f"{v[60 - m]} minutes to {v[h + 1]}"

if __name__ == '__main__':

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result)
