i = input()
li = []
for x in range(0,len(i)):
    li.append( i[x:] )
    li.sort()

for y in li:
    print(y)