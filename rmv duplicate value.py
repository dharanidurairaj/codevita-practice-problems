i/p: 5
1 2 3 1 2
o/p:
1 2 3




a=int(input())
l=[]
for i in range(0,a):
   l.append(int(input()))
for j in l:
   f=l.count(j)
   if f==1:
       print(list(j))

#same program:         
         
         
n=int(input())
l=[]
l1=[]
for i in range(0,n):
    b=input()
    l.append(b)
for i in l:
    if(1==l.count(i)):
        l1.append(i)
l=l1
print(l)
