d1,m1,y1  = map(int,input().split())
d2,m2,y2  = map(int,input().split())
if y1 - y2 > 0:
    print(10000)
elif y1 - y2 < 0:
    print(0)
elif m1 - m2 > 0:
    print(500*(m1-m2))
elif m1 - m2 < 0:
    print(0)
elif d1 - d2 > 0:
    print(15*(d1-d2))
else:
    print(0)