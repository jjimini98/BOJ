import sys

for line in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split( ))
    print("Case #%s:" %str(line+1) ,a + b)