def lopy(n,k):
    c = []
    d = []
    t = 1
    a = list(map(int,input().split()))
    c.append(a)
    for i in range(k-1):
        a = list(map(int, input().split()))
        for j in range(len(c)):
            if c[j].count(a[0]) == 1 and c[j].count(a[1]) == 0:
                c[j].append(a[1])
                break
            elif c[j].count(a[0]) == 0 and c[j].count(a[1]) == 1:
                c[j].append(a[0])
                break
            if j == len(c)-1 and c[j].count(a[0]) == 0 and c[j].count(a[1]) == 0:
                c.append(a)
    for i in range(len(c)):
        d.append(len(c[i]))
    for i in range(n):
        for j in range(len(c)):
            if c[j].count(i) > 0:
                t = 0
                break
            else:
                t = 1
        if t == 1:
            c.append(i)
            d.append(1)
    # print(c)
    d.sort()
    print(len(d))
    for i in range(len(d)):
        print(d[i],end=" ")
if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        k = int(input())
        try:
            lopy(n,k)
        except Exception:
            pass
        # lopy(n,k)