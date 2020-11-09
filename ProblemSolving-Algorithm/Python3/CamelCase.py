#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    i = 1
    for j in s:
        if j.isupper() == True:
            i += 1
    return i

if __name__ == '__main__':
    s = input()

    result = camelcase(s)
    print(result)