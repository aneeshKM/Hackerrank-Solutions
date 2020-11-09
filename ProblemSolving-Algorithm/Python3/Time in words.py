l1 = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twele","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
l2 = ["quarter","half","past","minutes","to"]
l3 = ["twenty","thirty","forty","fifty","sixty","seventy","hundred"]
h = int(input())
m = int(input())
if m == 0:
    print(l1[h],"o' clock")
elif m == 15:
    print(l2[0],l2[2],l1[h])
elif m == 30:
    print(l2[1],l2[2],l1[h])
elif m == 45:
    print(l2[0],l2[4],l1[h+1])
elif m < 19:
    if m != 1:
        print(l1[m],l2[3],l2[2],l1[h])
    else:
        print(l1[m], "minute", l2[2], l1[h])
elif m < 30:
    a,b = int(str(m)[0]),int(str(m)[1])
    a = l3[a-2]
    if b !=0:
        b = " "+l1[b]
    else:
        b = ""
    print(a+b,l2[3],l2[2],l1[h])
else:
    m = 60 - m
    if m != 1 and m < 15:
        print(l1[m],l2[3],l2[4],l1[h+1])
    elif m != 1 :
        a, b = int(str(m)[0]), int(str(m)[1])
        a = l3[a - 2]
        b = " " + l1[b]
        print(a+b, l2[3], l2[4], l1[h + 1])
    else:
        print(l1[m], "minute", l2[4], l1[h + 1])