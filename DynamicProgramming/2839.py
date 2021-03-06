N = int(input())

sugar = [5,3]
count = 0

for x in sugar:

   if N//x ==0 and x==3:
         count+=1
         break


   if x==sugar[0] & N//x==0:
      print(-1)
      break
    
   count += N //x 
   N = N %x

 
      
   
   
   
print(count)