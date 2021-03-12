# 구구단

import sys
number = int(sys.stdin.readline())

for n in range(1,10):
    print(str(number) , "*" , str(n) , "=", str(number * n))



# 내 예전 코드
# dan = int(input())
# result = 0
# for i in range(1,10):
#     result = dan * i
#     print('{} * {} = {}'.format(dan,i,result))