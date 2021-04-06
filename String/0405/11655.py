# Baekjoon Online Judge

sen = input().split(" ")
print(sen)
li = []
for x in sen :
    for t in x:
        li.append(chr(ord(t)+13))
    print(li)