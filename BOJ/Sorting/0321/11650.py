# 좌표 정렬하기
import sys

num = int(sys.stdin.readline())
x = [], y = []

def m_sort(lis,lis2) :  # 인자로 리스트가 들어가야함..
    for x,y in zip(sorted(lis),sorted(lis2)):
        print(x,y)


for _ in range(num):
    a,b = sys.stdin.readline().split(" ")
    x.append(int(a))
    y.append(int(b))
    m_sort(x,y)


