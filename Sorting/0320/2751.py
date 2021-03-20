# 2751 정렬

import sys

num = int(sys.stdin.readline())
lis = []
for _ in range(num):
    lis.append(int(input()))
lis.sort()
for i in lis:
    print(i)

