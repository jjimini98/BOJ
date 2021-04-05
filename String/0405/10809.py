import string

stri = input()


for x in string.ascii_lowercase:
    if x in stri:
        print(stri.index(x),end=" ")
    else:
        print(-1, end=" ")


