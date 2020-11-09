#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    l2 = []
    a = 0
    for i in  range(len(arr)):
        m = 0
        l1=[]
        while m != arr[i]:
            m += 1
            l1.append(m)
            if m % k == 0:
                l2.append(l1)
                l1 = []
        if l1 != []:
            l2.append(l1)
    for i in range (len(l2)):
        if l2[i].count(i+1) == 1:
            a += 1
    return a
if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)