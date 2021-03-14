# 별 찍기 -9

import sys

n = int(sys.stdin.readline())

for t in range(-n,0):
    print(" "*(n-abs(t)) + "*" * (2*abs(t)-1))

for i in range(2,n+1):
    print(" "*(n-i) + "*" * (2*i-1))



# 좀 더 나은 답안
# n = int(input())
#
# for i in range(n):
#     print(' '*i+'*'*((n-i)*2-1))
#
# for i in range(1, n):
#     print(' '*(n-1-i)+'*'*(i*2+1))