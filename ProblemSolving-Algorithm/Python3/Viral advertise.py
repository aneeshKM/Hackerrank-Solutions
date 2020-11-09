n = int(input())
likes = 0
share = 5//2
c = 0
for _ in range(n):
    likes += share
    share *= 3
    share = share//2
print(likes)