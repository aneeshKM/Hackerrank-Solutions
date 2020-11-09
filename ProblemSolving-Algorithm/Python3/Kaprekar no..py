def kaprekar(n,w):
    a = str(n*n)
    c = len(str(n))
    if len(a) == c:
        s = int(a)
    elif int(a[len(a)-c:len(a)]) != 0:
        d = int(a[len(a)-c:len(a)])
        s = int(a[:len(a)-c])+d
    else:
        s = "s"
    if n == s:
        print(n,end=" ")
        w.append(n)
if __name__ == '__main__':
    p = int(input())
    q = int(input())
    w = []
    for i in range(p,q+1):
        kaprekar(i,w)
    if len(w) == 0:
        print("INVALID RANGE")