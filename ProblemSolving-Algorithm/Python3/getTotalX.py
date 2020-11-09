#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    x = max(a)
    y = min(b)
    l1 = []
    k = 0
    for i in range(x,y+1):
        for j in range(len(a)):
            if i % a[j] != 0:
                j = 200
                break
        if j == len(a)-1:
            l1.append(i)
    for i in range(len(l1)):
        for j in range(len(b)):
            if b[j] % l1[i] != 0:
                j = 200
                break
        if j == len(b)-1:
            k += 1
    return k
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)
