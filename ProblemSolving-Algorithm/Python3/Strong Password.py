def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    a,b,c,d,f = 0,0,0,0,0
    for i in password:
        if i.islower() == True:
            a += 1
        elif i.isupper() == True:
            b += 1
        elif i.isalnum() == True:
            c += 1
        else:
            d += 1
    l1 = [a,b,c,d]
    e = l1.count(0)
    if n < 6:
        f = 6-n
        return max(e,f)
    else:
        return e
if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)