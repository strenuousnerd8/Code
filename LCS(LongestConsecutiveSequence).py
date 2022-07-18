# Return the length of longest consecutive sequence of integers in the list

l = [5, 6, 1, 2, 8, 9, 7]

import more_itertools as mit

def qsort(l):
    if not l:
        return l
    else:
        pivot = l[0]
        less = [i for i in l if i < pivot]
        more = [x for x in l[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)

l = qsort(l)

cons = [list(group) for group in mit.consecutive_groups(l)]
print(cons, end="\n\n")
print(max([len(i) for i in cons]))