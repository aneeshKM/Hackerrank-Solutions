num = int(input())
contacts = {}
for i in range(0, num):
    entry = input().split()
    name = entry[0]
    mob = int(entry[1])
    contacts[name] = mob

while True:
    # try:
    name = input()
    # except EOFError:
    #     break
    if name !="":
        if name in contacts:
            mob = contacts[name]
            print(name + "=" + str(mob))
        else:
            print("Not found")
    else:
        break