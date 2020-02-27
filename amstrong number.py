lower = int(input())
upper = int(input())

for num in range(lower, upper + 1):

  
   order = len(str(num))
    

   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
      -----------------------------------------------------------------------------------------------------------------------------------------

      
      
      
      a = int(input())
b = int(input())
for i in range(a, b + 1):
    d = 0
    temp = i
    while temp > 0:
        temp //= 10
        d+=1
    sum = 0
    temp = i
    while temp > 0:
        r = temp % 10
        sum += r ** d
        temp //= 10
    if i == sum:
        print(i,end=" ")
        
        --------------------------------------------------------------------------------------------------
        
        
        
        
import math
a = int(input())
b = int(input())
for i in range(a, b + 1):
    d = int(math.log10(i)+1)
    temp = i
    sum = 0
    temp = i
    while temp > 0:
        r = temp % 10
        sum += r ** d
        temp //= 10
    if i == sum:
        print(i,end=" ")
        
        
        -------------------------------------------------------------------------------------------------------
