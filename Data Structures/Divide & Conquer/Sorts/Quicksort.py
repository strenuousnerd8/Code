def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def swap(my_list, swap_index, i):
    temp = my_list[swap_index]
    my_list[swap_index] = my_list[i]
    my_list[i] = temp

def quicksort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        pivot(my_list, left, pivot_index - 1)
        pivot(my_list, pivot_index + 1, right)
    return my_list

def quicksort(my_list):
    return quicksort_helper(my_list, 0, len(my_list) - 1)

print(quicksort([4,6,1,7,3,2,5]))