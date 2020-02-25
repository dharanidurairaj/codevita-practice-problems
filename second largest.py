i/p:-840 -337 -1
o/p: -840




a=-10000
b=-10000
while(True):
    c=int(input())
    if(c==-1):
        break
    if(c>a):
        b=a
        a=c
    elif(c>b):
        b=c
print(b)
