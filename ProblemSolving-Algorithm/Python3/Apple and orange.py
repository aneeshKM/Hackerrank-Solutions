#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apl = 0
    orng = 0
    for i in range(len(apples) + len(oranges)):
        if i <= len(apples)-1:
            apples[i] = apples[i] + a
            if apples[i] >= s and apples[i] <= t:
                apl = apl + 1
        else:
            x = i - len(apples)
            if x < 0:
                x = x * (-1)
            oranges[x]= oranges[x] + b
            if oranges[x] >= s and oranges[x] <= t:
                orng = orng + 1
    print(apl)
    print(orng)
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
