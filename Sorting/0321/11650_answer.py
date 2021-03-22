# N = int(input())
# nums = []
# for i in range(N):
#     [a, b] = map(int, input().split())
#     nums.append([a, b])
#
# nums = sorted(nums)
# for i in range(N):
#     print(nums[i][0], nums[i][1])


import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
print(so)
so.sort(key=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])