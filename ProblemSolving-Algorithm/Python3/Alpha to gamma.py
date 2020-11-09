def encryption(msg):
    st = ""
    y = 0
    z = 0
    n = 0
    for i in range(len(msg)-1,-1,-1):
        x = 8*int(msg[i][0]) + 4*int(msg[i][1]) + 2*int(msg[i][2]) + 1*int(msg[i][3])
        st = st + "%" + str(x)
        y += x
    st = st[1:]
    # print(y)
    y = y+len(msg)-1
    while y>10:
        y = code(y)
    print(y)
    print(st)
def code(y):
    x = 0
    while True:
        y = str(y)
        for i in range(len(y)):
            x += int(y[i])
        break
    return int(x)
if __name__ == '__main__':
    msg = list(input().split())
    encryption(msg)