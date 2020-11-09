#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    i = 0
    a = len(s)
    b = ""
    while True:
        if s[i] == s[i+1]:
            i += 2
        else:
            b += s[i]
            i += 1
        if i+1 == len(s):
            break
    if len(b) == 0:
        return "Empty String"
    else:
        return b
if __name__ == '__main__':
    s = input()

    result = superReducedString(s)
    print(result)