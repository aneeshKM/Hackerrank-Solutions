# cook your dish here
def punish(nk):
    n = nk[0]
    k = nk[1]
    x = n-1
    p = 1
    if n >= k:
        return k
    else:
        while k-x>=n:
            x += n-1
            p += 1
        s = k - x
        if p%2 == 0:
            return s
        elif p%2 == 1:
            return n-s+1

if __name__ == '__main__':
    for i in range(int(input())):
        nk = list(map(int,input().split()))
        print(punish(nk))