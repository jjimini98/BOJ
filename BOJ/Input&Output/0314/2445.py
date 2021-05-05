# 별찍기 -8
import sys

number = int(sys.stdin.readline())

for x in range(1,number+1):
    print(("*" * x).ljust(number), end=""), print(("*" * x).rjust(number))
for x in range(-(number-1), 0):
    print(("*" * abs(x)).ljust(number), end=""), print(("*" * abs(x)).rjust(number))