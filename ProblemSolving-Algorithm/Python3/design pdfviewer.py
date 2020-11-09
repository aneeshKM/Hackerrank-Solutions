#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alpha = {}
    x = 97
    y = []
    for i in range(len(h)):
        alpha[x] = h[i]
        x += 1
    for i in range(len(word)):
        y.append(alpha[ord(word[i])])
    return max(y)*len(word)
if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
    print(result)
