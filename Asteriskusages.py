# 1. Unpacking Using *
print("1. Unpacking Using *")
nums = [i for i in range(1, 6)]
    ## a will be 1 and b will be a list containing remaining elements
a, *b = nums
print(a, b)
a, *b, c = nums
print(a, b, c)

# 2. combining a tuple, list, set
nums = [1, 2, 3]
nums2 = (4, 5, 6)
nums3 = {7, 8, 9}

    ## we convert the combined elements into any iterable we want
_list = [*nums, *nums2, *nums3]
_tuple = (*nums, *nums2, *nums3)
_set = {*nums, *nums2, *nums3}

print(type(_list))
print(_list)
print("------------------------")
print(type(_tuple))
print(_tuple)
print("------------------------")
print(type(_set))
print(_set)

