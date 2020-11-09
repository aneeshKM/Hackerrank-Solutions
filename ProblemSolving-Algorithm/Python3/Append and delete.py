#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    a = len(s)
    b = len(t)
    c = max(a,b)
    for i in range(c):
        try:
            if s[i] != t[i]:
                p = a + b - 2*(i)
                if k < p:
                    return "No"
                else:
                    return "Yes"
        except:
            if a<b:
                p = b - i
            elif b<a:
                p = a - i
            if k < p:
                return "No"
            elif (a % 2 == 0 and b % 2 == 1 or a % 2 == 1 and b % 2 == 0) and c/a !=2 or c/b != 2 :
                return "No"
            else:
                return "Yes"
    return "Yes"

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)
    print(result)