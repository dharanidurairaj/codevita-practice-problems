a=int(input())
b=[]
l=[]
p=0
for i in range(1,a):
    if a%i==0:
        b.append(i)
for j in b:
    d=j**2
    l.append(d)
for k in l:
    if k==a:
        p+=k
if p==a:
    
    print("Yes")
else:
    print("No")
    
    
    
    
