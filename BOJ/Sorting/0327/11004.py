#K번째 수
import sys

N,K = map(int, sys.stdin.readline().split(" "))

li = list(map(int, sys.stdin.readline().split(" "))) #string으로 받으면 틀림. 요소들을 int로 받기
li.sort()

print(li[K-1])
