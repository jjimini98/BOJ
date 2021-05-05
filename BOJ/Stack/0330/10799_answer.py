a = input()

s = []
b = 0

for i in range(len(a)):
    if a[i] == "(":
        s.append("(")
    else:
        if a[i-1] == "(":
            s.pop()
            b += len(s)

        else:
            s.pop()
            b += 1
print(b)
