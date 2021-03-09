# 숫자의 합
import sys

len_number = int(sys.stdin.readline())
number = sys.stdin.readline()
sum = 0

for x in range(len_number):
    sum += int(number[x])

print(sum)