
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # I just wrote a one-liner because it was too easy for branching and why not, we all love one liners
    return '00' + s[2:-2] if 'AM' in s and '12' in s else '12'+ s[2:-2] if 'PM' in s and '12' in s else s[:-2] if 'AM' in s else str(int(s[:2]) + 12) + s[2:-2]

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
