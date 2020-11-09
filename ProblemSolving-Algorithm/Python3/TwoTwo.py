def twoTwo(a):
    b = len(a)
    n = 2
    c = 0
    while True:
        c += a.count(str(n))
        n = n*2
        if len(str(n))>b:
            break
    return c
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        a = input()
        result = twoTwo(a)
        print(result)