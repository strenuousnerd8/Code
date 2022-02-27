stre = str(input())
A = str(input())
B = str(input())

#now lets slice from first occurence to last occurence of same alphabet in stre and return length of it
if B in stre[stre.index(A)+1:stre.rindex(A)]:
    print(len(stre[stre.index(A)+1:stre.rindex(A)]))