# ROT13

import string

al = string.ascii_lowercase
AL = string.ascii_uppercase

sen = input()
new_sen = ""
m = 97
n = 65
for x in sen:

        if ord(x) in list(range(97,123)) :

            if ord(x)+13 > 122:
                mi = abs(122-(ord(x)+13)+1)
                m = 97 + mi
                new_sen += chr(m)

            else: new_sen+= chr(ord(x)+13)

        elif ord(x) in list(range(65,91)):

            if ord(x)+13 > 90:
                mi = abs(90-(ord(x)+13)+1)
                m = 65 + mi
                new_sen += chr(m)

            else: new_sen += chr(ord(x) + 13)

        elif x == " " : new_sen += " "
        elif ord(x) in list(range(48,58)): new_sen += chr(ord(x))
        else:
            continue

print(new_sen)