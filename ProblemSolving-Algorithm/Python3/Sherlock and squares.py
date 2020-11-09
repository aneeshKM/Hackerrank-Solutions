import math
for _ in range(int(input())):
    n,m = map(int,input().split())
    n,m = math.ceil(math.sqrt(n)),math.floor(math.sqrt(m))
    print(m-n+1)