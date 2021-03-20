import sys

count = int(sys.stdin.readline())

N = list(map(int,sys.stdin.readline().split(" ")))

print(min(N),max(N))
