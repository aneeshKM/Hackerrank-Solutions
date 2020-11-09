def gift(b,w,bc,wc,z):
    a = b*bc + w*wc
    c = (b+w)*bc + z*w
    d = (b+w)*wc + z*b
    l1 = [a,c,d]
    return min(l1)
if __name__ == '__main__':
    for i in range(int(input())):
        b,w = map(int,input().split())
        bc,wc,z = map(int,input().split())
        a = gift(b,w,bc,wc,z)
        print(a)