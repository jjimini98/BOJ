import sys

number = map(int, sys.stdin.readline())
print(number)

for x in range(1,number):
    print("*" * x)


#Traceback (most recent call last):
#   File "C:/Users/jimin/PycharmProjects/BOJ/입출력/0313/practice.py", line 6, in <module>
#     for x in range(1,number):
# TypeError: 'map' object cannot be interpreted as an integer
# <map object at 0x0000029C3D70D4E0>