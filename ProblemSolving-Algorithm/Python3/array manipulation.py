n,q = map(int,input().split())
a = []
b = {}
for _ in range(q):
    c = list(map(int,input().split()))
    a.append(c)
    b[c[0]] = 0
    b[c[1]] = 0
res = dict(sorted(b.items()))
e = list(res.keys())
for i in a:
    x = e.index(i[0])
    y = e.index(i[1])
    for j in range(x,y+1):
        res[e[j]] += i[2]
print(max(res.values()))