#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v2 >= v1 :
        return "NO"
    else:
        while True:
            x1 = x1 + v1
            x2 = x2 + v2
            if x1==x2:
                return "YES"
                break
            elif x1>x2:
                return "NO"
                break
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    # fptr.write(result + '\n')
    print(result)
    # fptr.close()
