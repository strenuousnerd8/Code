def mostRepeatingString(str):
    lis = str.split()
    counter = []
    for i in lis:
        counter.append(lis.count(i))
    index = counter.index(max(counter))
    return ' '.join(list(filter((lis[index]).__ne__, lis)))

print(mostRepeatingString(str(input())))