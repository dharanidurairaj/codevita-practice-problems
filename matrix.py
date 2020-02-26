i/p:
1
2
3
4
o/p:
0 1 
2 3




r=2
c=2
b=[[0 for i in range(r)]for i in range(c)]
for i in range(0,r):
    for j in range(0,c):
        b[i][j]=int(input())
for i in range(0,r):
    for j in range(0,c):
        print(b[i][j],end=" ")
    print(" ")
