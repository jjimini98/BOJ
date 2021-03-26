import sys

num = int(sys.stdin.readline())
li = []
result = []

for _ in range(num):
    li.append(int(sys.stdin.readline()))
li.sort()
# print(li)

for x in range(len(li)):
    result.append(li.count(li[x]))
    # print(result)
max_num = li[max(result)-1]
print(max_num)