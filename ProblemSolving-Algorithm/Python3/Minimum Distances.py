def dist(n,a):
    b = n+1
    d = {}
    for i in range(n):
        try:
            d[a[i]] += 1
            b = min(i-a.index(a[i]),b)
        except:
            d[a[i]] = 1
    if b == n+1:
        return -1
    else:
        return b
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    result = dist(n,a)
    print(result)