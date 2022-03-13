#!/bin/python3

import enum
import math
import os
import random
import re
from sre_parse import parse_template
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    k-=1
    arr.sort()
    return min(arr[i+k]-arr[i] for i in range(len(arr)-k))

if __name__ == '__main__':

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(str(result) + '\n')
