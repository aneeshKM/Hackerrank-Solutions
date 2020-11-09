import math
def encryption(s):
    r = math.floor(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))
    if r*c < len(s):
        if r<c:
            r += 1
        else:
            c += 1
    l1 = []
    n = 0
    for i in range(r):
        try:
            l1.append(s[n:n+c])
            n = n+c
        except:
            l1.append(s[n:len(s)])
    l2 = []
    a = ""
    for j in range(c):
        for i in l1:
            try:
                a += i[j]
            except:
                break
        l2.append(a)
        a = ""
    return l2
if __name__ == '__main__':
    s = input()
    result = encryption(s)
    for i in result:
        print(i,end=" ")