n,d = map(int,input().split())
l,k = list(map(int,input().split())),0
while n-k!=0:
    print(l[d],end=" ")
    d += 1
    k += 1
    if d == len(l):
        d = 0