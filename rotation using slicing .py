i/p:5
1 2 3 4 5 
2
o/p:
4 5 1 2 3



a=int(input())
b=list(map(str,input().split(" ")))
c=int(input())
d=b[0:len(b)-c]
e=b[len(b)-c:]
print(e+d)

########same without slicing

a=int(input())
b=list(map(str,input().split(" ")))
c=int(input())
l=[]
for i in range(len(b)-c,len(b)):
   l.append(b[i])
for j in range(0,len(b)-c):
   l.append(b[j])
print(l)


#using algorithm


n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
r=int(input())
for i in range(0,r):
    t=a[n-1]
    u=n-1
    while(u>=0):
        a[u] = a[u-1]
        u = u-1
    a[0] = t
print(a)
