def result(n,a):
    d = {}
    for i in a:
        try:
            d[i] += 1
        except:
            d[i] = 1
    b = max(list(d.values()))
    if  b == 1:
        return n-1
    else:
        return n - b
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    print(result(n,a))