# For even number of items in list
t = [1,2,3,4,5,6,7]
divisions = 2
res = [t[i:i+divisions] for i in range(0, len(t), divisions)]
print(res)