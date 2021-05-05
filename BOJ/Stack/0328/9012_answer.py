for _ in range(int(input())):
    stack = []
    vps = input()
    check = 0

    for c in vps:
        if c == "(":
            stack.append(c)

        elif c == ")":
            if len(stack) == 0: # 아무것도 없는데 ")"를 추가하면 vps를 만족할 수 없음.
                print("NO") # ) 로 시작하면 쨌든 vps를 만족못하므로 NO 출력
                check = 1
                break

            else:
                stack.pop(-1) # stack에 ( 가 있다면, 맨 마지막에 있는 ( 를 pop 제거.

         # for 문을 돌면서 (는  stack에 추가하고 )가 등장했을 때 짝이 맞으면 stack에서 제거. ( 와 )가 짝이 안맞다면 NO 출력

    if len(stack) != 0 and check == 0: print("NO")  # 맨 마지막에 stack에 요소가 남아있고 check 값이 0 이면 NO 출력
    elif len(stack) == 0 and check == 0: print("YES") # stack 에 값이 아무것도 남아있지 않고 check 값이 0 이면 YES 출력  --> 가상 이상적

