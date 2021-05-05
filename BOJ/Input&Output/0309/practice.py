import  sys

sentence = sys.stdin.readline()

for x in range(0,len(sentence)):
    if (x+1) % 10 == 0:
        print(sentence[x], "\n")
