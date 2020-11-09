#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    l3 = []
    l2 = []
    l1 = []
    for k in range(len(P)):
        for i in range(len(G)):
            if G[i].find(P[k]) == -1:
                l1.append([])
            else:
                m = 0
                while m != -1 and m < len(G[i]):
                    m = G[i].find(P[k], m)
                    print(m)
                    if m != -1:
                        l2.append(m)
                        m += 1
                l1.append(l2)
                l2 = []
        l3.append(l1)
        l1 = []
    for i in range(len(l3)):
        l3[i] = l3[i][i:]
    while True:
        try:
            l4 = []
            for i in range(len(l3)):
                l4.append(l3[i][0])
            if min(l4) != []:
                for i in range(len(min(l4))):
                    y = 0
                    for j in range(len(l4)):
                        y += l4[j].count(min(l4)[i])
                    if y == len(l4):
                        return "YES"
                        break
            for i in range(len(l3)):
                l3[i] = l3[i][1:]
        except IndexError:
            return "NO"
            break
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)

