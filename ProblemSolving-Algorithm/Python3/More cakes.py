def cakes(snkr):
    s = snkr[0]
    n = snkr[1]
    k = snkr[2]
    r = snkr[3]
    x = k
    for i in range(n-1):
        x += k*r
        k = k*r
    if x <= s:
        print("POSSIBLE", s - x)
    else:
        print("IMPOSSIBLE", x - s)
    return s - x
if __name__ == '__main__':
    t = int(input())
    z = 0
    for i in range(t):
        snkr = list(map(int,input().split()))
        p = cakes(snkr)
        z += p
    if z >= 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")