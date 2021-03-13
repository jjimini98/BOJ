import sys

number = map(int, sys.stdin.readline())

for x in range(1,number):
    print("*" * x)