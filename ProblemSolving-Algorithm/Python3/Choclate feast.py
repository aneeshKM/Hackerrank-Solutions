def feast(n,c,m):
    y = n // c
    n = n // c
    if n >= m:
        while n >= m:
            y = y + n // m
            n = n // m + n % m
    else:
        n = 1
    print(round(y))
if __name__ == '__main__':
    for i in range(int(input())):
        ncm = list(map(int,input().split()))
        n = ncm[0]
        c = ncm[1]
        m = ncm[2]
        feast(n,c,m)