while True :
    stack = []
    example = input()

    for x in example:
        if x == "(":
            stack.append(x)
            if x+1 == ")":break



                # 진행중 !! 아직 안끝남