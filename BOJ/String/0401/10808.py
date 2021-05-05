#알파벳 개수
import string


sten = input()
lis = [0 for _ in range(26)]
alpha_dict = {idx : alpha for idx , alpha in enumerate(string.ascii_lowercase)}
for y in alpha_dict.items():
    for x in sten :
        if x == y[1]:
            lis[y[0]] +=1


for t in lis:
    print(t, end=" ")