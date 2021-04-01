#알파벳 개수
from collections import Counter
import string



sten = input()
alpha = string.ascii_lowercase
lis = []

for a in alpha:
    for s in sten :
        if a == s:
            lis.insert(alpha.find(a),sten.count(s))
        else:
            lis.insert(alpha.find(a),sten.count(s))
print(lis)
print(len(lis))
