#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, q):
    d = {}
    for i in q:
        for j in range(i[0],i[1]+1):
            try:
                d[j] += i[2]
            except:
                d[j] = 0
                d[j] += i[2]

    return max(d.values())
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):

        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)