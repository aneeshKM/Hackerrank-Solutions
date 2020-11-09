n,q = map(int,input().split())
la = 0
l = []
for _ in range(n):
    l.append([])
for _ in range(q):
    a,x,y = map(int,input().split())
    if a == 1:
        p = ((x^la)%n)
        l[p].append(y)
    else:
        p = (x^la)%n
        la = l[p][y%len(l[p])]
        print(la)
