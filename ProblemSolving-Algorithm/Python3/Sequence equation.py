n = int(input())
a = list(map(int,input().split()))
b = [0]
for i in a:
    b.append(i)
for i in range(1,n+1):
    a = b.index(i)
    a = b.index(a)
    print(a)
