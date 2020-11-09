def lotr(x,y):
    n = int(str(x)+str(y))
    if (x*y)+x+y == n:
        return 1
    else:
        return 0
def lot(m,n):
    k = 0
    t = 0
    p = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            k += lotr(i,j)
        if k!=t:
            p += 1
            t = k
    print(k,p)
if __name__ == '__main__':
    for i in range(int(input())):
        mn = list(map(int,input().split()))
        m = mn[0]
        n = mn[1]
        lot(m,n)