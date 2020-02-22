i/p:abcdde@gmail.com
o/p:valid

i/p:xyz@yahoo.com
o/p:not vallid



a=input()
b="@"
c="."
d=a.index(b)
e=a.index(c)
f=a[0:d]
g=len(f)
h=a[d:e]
i=len(h)
j=a[e:]
k=len(j)
if(g>=6 and i>3 and k==4):
    print("valid")
else:
    print("Not valid")
