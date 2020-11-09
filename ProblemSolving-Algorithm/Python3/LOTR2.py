from itertools import product
def lotr(x,y):
    n = int(str(x)+str(y))
    if (x*y)+x+y == n:
        print(x,y)
        return 1
    else:
        return 0
def lot(m,n):
    k = 0
    t = 0
    p = 0
    x = 0
    a = []
    b = []
    for i in range(1,m+1):
        a.append(i)
    for i in range(1,n+1):
        if i%9 == 0:
            b.append(i)
    print(b)
    print(len(b))
    print(k,m)
if __name__ == '__main__':
    for i in range(int(input())):
        mn = list(map(int,input().split()))
        m = mn[0]
        n = mn[1]
        lot(m,n)