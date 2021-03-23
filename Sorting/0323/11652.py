#11652 카드
import sys

num = int(sys.stdin.readline())
li = [0 for _ in range(num)]

for x in range(num):
    num = int(sys.stdin.readline())
    if num < 0  :
        num1=abs(num)
        li[num1]+=1
    else:
        li[num] += 1
max_num = li.index(max(li))

if num<0:
    print(-max_num)
else:
    print(max_num)

