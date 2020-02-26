i/p:12
o/p:
1 2 2 3




n=int(input())
i=1
while(i<=n):
    if(n%i==0):
        n=n//i
        print(i)
        i=1
    i=i+1
