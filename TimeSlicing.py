def timeCon(take):
    time = take.split('-')
    _1st, _2nd = time[0][0:-2], time[1][0:-2]
    hour, minute = timeAdd(_1st, _2nd)
    if hour > 12 and hour <= 23:
        Meridiem = 'PM'
        hour -= 12
    else:
        Meridiem = 'AM'
    if minute < 10:
        minute = str(minute) + '0'
    elif minute > 60:
        minute -= 60
    return str(hour) + ":" + str(minute) + Meridiem

def timeAdd(t1, t2):
    t1 = t1.split(':')
    t2 = t2.split(':')
    a, b = t1[0], t1[1]
    x, y = t2[0], t2[1]
    hour = int(a) + int(x)
    minute = int(b) + int(y)
    return hour, minute

print(timeCon(str(input())))