#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    x=0

    y=0
    if m<n:
        x=s+m-1
        if x<=n:
            return x
        else:
            return x-n
    else:
        y=s+m-1
        x=y%n
        if x!=0:
            return x
        else:
            return n
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        # fptr.write(str(result) + '\n')
        print(result)
    # fptr.close()
