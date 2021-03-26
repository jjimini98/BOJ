n = int(input())
dic = {}

for case in range(n):
    tmp = int(input())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])