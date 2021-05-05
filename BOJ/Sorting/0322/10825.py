#10825 국영수
import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(sys.stdin.readline().split(" "))

li.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for t in li :
    print(t[0])
