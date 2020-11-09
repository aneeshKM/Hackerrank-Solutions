def flatland(n,m,a):
    a.sort()
    maxa = 0
    for i in range(m-1):
        maxa = max(maxa,abs((a[i]-a[i+1]))//2)
    maxa = max(maxa,abs(0-a[0]))
    maxa = max(maxa, abs(n-1 - a[m-1]))
    return maxa
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if m == n:
        print(0)
    else:
        result = flatland(n,m,a)
        print(result)