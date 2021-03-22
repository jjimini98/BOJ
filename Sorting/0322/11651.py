# 좌표 정렬하기 2
import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda x: (x[1],x[0]))

for i in li:
    print(i[0], i[1])