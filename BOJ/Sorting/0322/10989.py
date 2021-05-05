#10989 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
ar = []
for x in range(n):
    ar.append(int(sys.stdin.readline()))
    sorted(ar)
    print(ar[x])

