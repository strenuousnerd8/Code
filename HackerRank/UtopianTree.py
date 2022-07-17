#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    my_dict = {i : 0 for i in range(n + 1)}
    switch = {True : False, False : True}
    count = 1
    flag = True
    for i in my_dict.keys():
        if i != 0:
            if flag:
                flag = switch[flag]
                my_dict[i] = count + count
                count = my_dict[i] + 1
            else:
                flag = switch[flag]
                my_dict[i] = count
        else:
            my_dict[i] = 1
            continue

    return list(my_dict.values())[-1]

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(str(result) + '\n')