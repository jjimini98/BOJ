import sys
from collections import deque

q = deque([])

for _ in range(int(sys.stdin.readline())):
    case = sys.stdin.readline()
    if "push" in case :
        a,b = case.split(" ")
        q.append(int(b))
    elif case == "size\n":
        print(len(q))
    elif case == "pop\n":
        if len(q) == 0 : print(-1)
        else: print(q.popleft())
    elif case == "empty\n":
        if len(q) == 0 : print(1)
        else : print(0)
    elif case == "front\n":
        if len(q) == 0:print(-1)
        else:print(q[0])
    elif case == "back\n":
        if len(q) == 0: print(-1)
        else : print(q[len(q)-1])