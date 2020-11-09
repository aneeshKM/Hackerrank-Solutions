n = int(input())
a = list(map(int,input().split()))
count = 0
for i in a:
    c = a.count(i)
    ct = a.count(i + 1)
    cn = a.count(i - 1)
    b = c + ct
    d = c + cn
    if count < b or count < d:
        if b >= d:
            count = b
        else:
            count = d
print(count)