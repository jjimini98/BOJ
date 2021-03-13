number = int(input())

print(("*" ).center(number))
for x in range(1,number):
    print("{:^1}".format(("*" * (2*x +1))))



# 정답
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i) + "*" * (2*i-1))