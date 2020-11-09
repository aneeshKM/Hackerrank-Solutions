def pageCount(n, p):
    a = p//2
    if n//2-p//2 < p//2:
        a = n//2-p//2
    return a
if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print(result)