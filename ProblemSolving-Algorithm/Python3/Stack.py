x= int(input())
stack = []
max_st = [-1]
for i in range(x):
    z = list(map(int,input().split()))
    if z[0] == 1:
        stack.append(z[1])
        if(z[1]) > max_st[len(max_st)-1]:
            max_st.append(z[1])
    elif z[0] == 2:
        if (stack[len(stack)-1]==max_st[len(max_st)-1] and stack.count(len(stack)-1) == 1):
            max.pop(len(max_st)-1)
        stack.pop(len(stack)-1)
    elif z[0] == 3:
        print(max_st[len(max_st)-1])
    z=[]
