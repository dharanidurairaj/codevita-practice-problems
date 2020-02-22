a=input()
b=['a','e','i','o','u','A','E','I','O','U']
l=[]
l1=[]
for i in a:
    if(i==" "):
        l.append(i)
        l1.append(i)
    if i in b:
        l.append(i)
    if i not in b:
        l1.append(i)
for j in l:
    print(j,end="")
print()
for k in l1:
    print(k.swapcase(),end="")
