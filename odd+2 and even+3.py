i/p:20
o/p:0 0 2 1 4 2 6 3 8 4 10 5 12 6

a=int(input())
d=a//2
l=[]
e=1
b=1
c=1
l.append(e)
l.append(b)
while(c<d):
    d1=e+2
    d2=b+3
    l.append(d1)
    l.append(d2)
    e=d1
    b=d2
    c+=1
for i in l:
    print(i,end=" ")
    
