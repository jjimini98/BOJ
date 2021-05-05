#스택

class Stack:
    def __init__(self):
        self.st_list = []
    def push(self,i):
        self.st_list.append(i)
        return self.st_list
    def pop(self):
        if len(self.st_list) == 0: return -1
        else: return self.st_list.pop()
    def size(self):
        return len(self.st_list)
    def empty(self):
        if len(self.st_list) == 0: return 1
        else: return 0
    def top(self):
        if len(self.st_list) == 0: return -1
        else: return self.st_list[len(self.st_list)-1]


import sys

count = int(sys.stdin.readline())
s = Stack()

for _ in range(count):
    command = input()

    if command == "top":
        print(s.top())
    elif command == "size" :
        print(s.size())
    elif command == "pop":
        print(s.pop())
    elif command == "empty":
        print(s.empty())
    elif "push" in command:
        s.push(int(command[5]))
