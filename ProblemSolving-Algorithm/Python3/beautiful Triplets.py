def triplet(a,b,c):
    count = 0
    for i in c:
        if c.count(i+b) >= 1 and c.count(i+2*b) >= 1:
            count += 1
    return count
if __name__ == '__main__':
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    d = triplet(a,b,c)
    print(d)