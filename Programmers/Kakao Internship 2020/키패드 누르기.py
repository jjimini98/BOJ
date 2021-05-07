def solution(numbers, hand):
    answer = ''
    L=0
    R=0 
   


    for x in numbers:
         re = abs(R-x)
         le = abs(L-x)
         if x in [1,4,7]:
            answer += "L"
            L=x
         elif x in [3,6,9]:
            answer += "R"
            R=x 
         if x in [2,5,8,0]:
            if re > le :
               if re in [2,5,8,0]:
                  answer+="R"
                  R=x
               answer+="L"
               L=x 
            elif re < le:
               if le in [2,5,8,0]:
                  answer += "L"
                  L=x
               answer += "R"
               R=x 
            
            elif re == le and hand == 'right':
                answer += "R"
                R =x 
            elif re == le and hand == "left":
                answer +="L"
                L=x 

    return answer


print(solution(	[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
