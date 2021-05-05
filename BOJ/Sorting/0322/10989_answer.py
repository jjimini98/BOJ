# 10989 수 정렬하기
import sys

N = int(sys.stdin.readline())
cnt_list = [0] * 10001

for _ in range(N):
    cnt_list[int(sys.stdin.readline())] += 1
print(cnt_list)
for i in range(10001):
    sys.stdout.write('%s\n' % i * cnt_list[i])