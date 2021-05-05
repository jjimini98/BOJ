import sys

count = int(sys.stdin.readline())
li = []

for _ in range(count):
    command = sys.stdin.readline()

    if command == "top\n":
        if len(li) == 0:
            print(-1)
        else:
            print(li[len(li)-1])

    elif command == "size\n" :
        print(len(li))
    elif command == "pop\n":
        if len(li) == 0: print(-1)
        else: print(li.pop())
    elif command == "empty\n":
        if len(li) == 0:
           print(1)
        else:
            print(0)
    elif "push" in command:
        a,b = command.split(" ")
        li.append(int(b))
