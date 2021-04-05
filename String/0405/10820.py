import sys

for X in sys.stdin:
    small = 0
    big = 0
    number = 0
    blank = 0
    for x in X:
            if ord(x) in list(range(97,123)):
                small+=1
            elif ord(x) in list(range(65,91)):
                big+=1
            elif x== " ":
                blank+=1
            elif ord(x) in list(range(48,58)):
                number+=1
            else: break
    print(small, big, number, blank)