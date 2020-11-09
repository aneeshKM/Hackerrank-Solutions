# cook your dish here
def punish(nk):
    n = nk[0]
    p = nk[1]
    x = 0
    k = 1
    for i in range(p):
        if k == 1:
            x += 1
        elif k == 0:
            x -= 1
        if x == 0:
            k = 1
            x = 2
        elif x == n+1:
            k = 0
            x = n-1
    return x
if __name__ == '__main__':
    for i in range(int(input())):
        nk = list(map(int,input().split()))
        print(punish(nk))