i/p:relearnpro
o/p:prorelearn



s1=input()
s2=input()
a=[]
for i in range(0,len(s1)):
    r=s1[i+1: ]+s1[ :i+1]
    if r==s2:
        a.append(r)
if len(a)==0:
    print("0")
else:
    print("1")
