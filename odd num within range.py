i/p:3
o/p:1
3




a=int(input())
for i in range(0,a+1):
    if(i%2!=0):
        print(i)
    
    
i/p:3
o/p:1
3
5



def odd(i,n):
    if(i<n):
        print(2*i+1)
        i=i+1
        odd(i,n)
n=int(input())
odd(0,n)
    
    
    
   ------------------------------------------------------------------------- 
    
    
    i=0
def odd(n):
    global i
    if(i<n):
        print(2*i+1)
        i=i+1
        odd(n)
n=int(input())
odd(n)
    
