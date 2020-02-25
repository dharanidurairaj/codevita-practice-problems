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
