def howManyGames(p, d, m, s):
    count = 0
    cash = 0
    while cash <= s:
        count += 1
        cash += p
        p -= d
        if p < m:
            p = m
    return count - 1
if __name__ == '__main__':
    pdms = input().split()
    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])
    answer = howManyGames(p, d, m, s)
    print(answer)