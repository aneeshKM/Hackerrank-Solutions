if __name__ == '__main__':
    n,q = map(int,input().split())
    a = [0]*(n+1)
    d = 0
    for _ in range(q):
        c = list(map(int,input().split()))
        a[c[0]] += c[2]
        if c[1]+1 <= n:
            a[c[1]+1] -= c[2]
    b = 0
    for i in range(n+1):
        b += a[i]
        if b>d:
            d = b
    print(d)