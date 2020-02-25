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
