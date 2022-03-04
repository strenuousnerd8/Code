#This is to exemplify that function call's return values can be
#accessed using indexes because functions return a tuple and tuple
#can be used like below
#tup = ("this", "is", 55)
#print(tup[0])

def sumsub(a, b):
	sum = a + b
	sub = a - b
	return sum, sub

print("sum is ", sumsub(2,2)[0])
print("sub is ", sumsub(2,2)[1])