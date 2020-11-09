# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    move = 2*n-2 + min(abs(1-r_q),abs(1-c_q)) + min(abs(n-r_q),abs(n-c_q)) +min(abs(1-r_q),abs(n-c_q))+min(abs(1-c_q),abs(n-r_q))
    x,y,g,h,l,m,o,p = n+1,n+1,n+1,n+1,n+1,0,n+1,0
    a,b,c,d,e,f,v,w = 0,0,0,0,0,0,0,0,
    for i in obstacles:
        if i[0] == r_q :
            if i[1] > c_q:
                if i[1] < x:
                    a = i[0]
                    x = i[1]
            elif i[1] < c_q:
                if i[1] < y:
                    b = i[0]
                    y = i[1]
        elif i[1] == c_q:
            if i[0] > r_q:
                if i[0] < g:
                    g = i[0]
                    c = i[1]
            elif i[0] < r_q:
                if i[0] < h:
                    h = i[0]
                    d = i[1]
        elif i[0]-r_q == i[1]-c_q:
            if i[0]>r_q:
                if i[0]<l:
                    l = i[0]
                    e = i[1]
            elif i[0]<r_q:
                if i[0]>m:
                    m = i[0]
                    f = i[1]
        elif abs(i[0]-r_q) == abs(i[1]-c_q):
            if i[0]>r_q:
                if i[0]<o:
                    o = i[0]
                    v = i[1]
            elif i[0]<r_q:
                if i[0]>p:
                    p = i[0]
                    w = i[1]
    l1 =[[a,x],[b,y],[g,c],[h,d],[l,e],[m,f],[o,v],[p,w]]
    for i in l1:
        if (i[0] != 0 and i[0] != n+1) and (i[1] != 0 and i[1] != n+1):
            if i[0] == r_q:
                if i[1] > c_q:
                    move -= (n-i[1]+1)
                elif i[1] < c_q:
                    move -= (i[1] - 1 + 1)
            elif i[1] == c_q:
                if i[0] > r_q:
                    move -= (n - i[0] + 1)
                elif i[0] < r_q:
                    move -= (i[0] - 1 + 1)
            elif i[0] - r_q == i[1] - c_q:
                if i[0] > r_q:
                    move -= (n-max(i)+1)
                elif i[0] < r_q:
                    move -= (min(i)-1+1)
            elif abs(i[0] - r_q) == abs(i[1] - c_q):
                if i[0] > r_q:
                     move -= (min((n-i[0]),(i[1]-1)) + 1)
                elif i[0] < r_q:
                    move -= (min((n-i[1]),(i[0]-1)) + 1)

    return move
if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)