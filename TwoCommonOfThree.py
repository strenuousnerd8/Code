# Print maximum of atleast 2 common elements in 3 sorted arrays
def get(a, b, c):
    overall = a + b + c
    overall = set(overall)
    res = []
    for i in overall:
        if(
            a.count(i) and b.count(i) or b.count(i) and c.count(i) or c.count(i) and a.count(i)
            ):
            res.append(i)
    return max(res)

# Driver Code
a = [ 1, 1, 2, 3, 4 ]
b = [ 2, 3, 5 ]
c = [ 3, 6 ]
print(get(a, b, c))