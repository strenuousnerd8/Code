# Quicksort in one line using list comprehension and recursion. Not truly optimal.

def qsort(lis):
    return (qsort([y for y in lis[1:] if y < lis[0]]) + lis[:1] + qsort([y for y in lis[1:] if y >= lis[0]])) if len(lis) > 1 else lis

print(qsort([4,6,1,7,3,2,5]))

# For better Readability
# return (qsort([y for y in lis[1:] if y < lis[0]]) +
#         lis[:1] +
#         qsort([y for y in lis[1:] if y >= lis[0]])) if len(lis) > 1 else lis