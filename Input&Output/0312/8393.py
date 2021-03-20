import sys


number = int(sys.stdin.readline())
sum = 0

for x in range(number+1):
    sum+=x

print(sum)