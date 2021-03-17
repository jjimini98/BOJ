import sys

number = int(sys.stdin.readline())
count = 0

while True:
    if number %2 ==0 and number % 5 !=0 :
        number  = number//2
        count +=1
        if number ==1 :
            print(count)
            break
        if number % 2 ==0:
            number = number //2
            count += 1
            if number == 1:
                print(count)
                break
        elif number % 3 ==0 :
            number = number //3
            count += 1
            if number == 1:
                print(count)
                break
        else:
            number -= 1
            count += 1
            if number == 1:
                print(count)
                break

    elif number %3 ==0:
        number = number//3
        count += 1
        if number == 1:
            print(count)
            break
        if number % 2 == 0:
                number = number // 2
                count += 1
                if number == 1:
                    print(count)
                    break
        elif number % 3 == 0:
                number = number // 3
                count += 1
                if number == 1:
                    print(count)
                    break
        else:
                number -= 1
                count += 1
                if number == 1:
                    print(count)
                    break

    else :
        number -=1
        count += 1
        if number == 1:
            print(count)
            break
        if number % 2 == 0:
                number = number // 2
                count += 1
                if number == 1:
                    print(count)
                    break
        elif number % 3 == 0:
                number = number // 3
                count += 1
                if number == 1:
                    print(count)
                    break
        else:
                number -= 1
                count += 1
                if number == 1:
                    print(count)
                    break






# def nanugi2(number):
#     number = number //2
#
#     if number==1:
#
#
#
#     return nanugi2(number)
#
# def nanugi3(number):
