a,b,k = map(int,input().split())
c = 0
for i in range(a,b+1):
    j = int(str(i)[::-1])
    if abs(i-j)%k == 0:
        c += 1
print(c)
