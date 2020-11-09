n,k,q = map(int,input().split())
a = list(map(int,input().split()))
for _ in range(q):
    i = int(input())
    c = i-k%n
    print(a[c])
