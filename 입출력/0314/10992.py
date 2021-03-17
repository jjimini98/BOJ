import sys

n = int(sys.stdin.readline())

for i in range(1,n+1):

    if i >=3 :
        # print(" " * (n - 1) + "*" * (2 * 1 - 1))
        print(" " * (n - i)  + "*" + " " * i + "*")
        print(" " * (n-(i+1)) + "*" * (2 * i - 1))
        break

    else:
        print(" " * (n - i) + "*" * (2 * i - 1))