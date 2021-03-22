#10814. 나이순 정렬
import sys

n = int(sys.stdin.readline())
usrs_li = []

for _ in range(n):
    usrs_li.append(sys.stdin.readline().split(" "))
usrs_li.sort(key= lambda x : (int(x[0])))

for t in usrs_li:
    print(t[0],t[1], end="")