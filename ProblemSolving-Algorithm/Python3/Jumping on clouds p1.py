n = int(input())
a = list(map(int,input().split()))
count = 0
i = 0
while True:
    if i+2 < len(a) and a[i+2] == 0:
        i += 2
        count += 1
    elif i+2 < len(a) and a[i+2] == 1:
        i += 1
        count += 1
    if i >= len(a) - 1:
        break
    elif i == len(a) - 2:
        count += 1
        break
print(count)