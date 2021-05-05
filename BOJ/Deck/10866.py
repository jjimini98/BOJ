import sys
from collections import deque

d = deque([])

for _ in range(int(sys.stdin.readline())):
    case = sys.stdin.readline()
    if "push" in case:
        a,b = case.split(" ")
        if a == "push_front" :
            d.appendleft(int(b))
        elif a == "push_back":
            d.append(int(b))
    elif case == "pop_front\n":
        if len(d) == 0 : print(-1)
        else: print(d.popleft())
    elif case == "pop_back\n":
        if len(d) == 0 : print(-1)
        else: print(d.pop())
    elif case == "size\n":
        print(len(d))
    elif case == "empty\n":
        if len(d) == 0 : print(1)
        else : print(0)
    elif case == "front\n":
        if len(d) == 0 : print(-1)
        else : print(d[0])

    elif case == "back\n":
        if len(d) == 0 :print(-1)
        else : print(d[len(d)-1])
