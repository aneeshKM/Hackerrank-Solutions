from itertools import combinations
# Complete the acmTeam function below.
def acmTeam(topic):
    a = 0
    b = 99999
    c = list(combinations(topic,2))
    l1 = []
    for i in c:
        l1.append(str(i[0]+i[1])[1:])
    for i in l1:
        if i.count("0")<b:
            a = 1
            b = i.count("0")
        elif i.count("0") == b:
            a += 1
    l2 = [len(l1[0])-b,a]
    return l2
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    topic = []
    for _ in range(n):
        topic_item = "1"+input()
        topic.append(int(topic_item))
    result = acmTeam(topic)
    print(result[0])
    print(result[1])