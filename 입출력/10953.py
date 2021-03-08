import sys
N = int(sys.stdin.readline())
for line in sys.stdin:
     a, b = map(int, line.split(","))
     print(a + b)