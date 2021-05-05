import sys
import queue

queue  = []

for _ in range(int(sys.stdin.readline())):
    case = sys.stdin.readline()
    if "push" in case :
        # a, b = case.split(" ")
        # queue.append(int(b))
         queue.append(int(case[5:]))
    elif case == "pop\n" :
        if len(queue) == 0 : print(-1)
        else: print(queue[0]), queue.remove(queue[0])
    elif case == "size\n" :
        print(len(queue))
    elif  case == "empty\n":
        if len(queue) == 0 : print(1)
        else : print(0)
    elif case == "front\n":
        if len(queue) == 0 : print(-1)
        else : print(queue[0])
    elif case == "back\n":
        if len(queue) == 0: print(-1)
        else : print(queue[len(queue)-1])