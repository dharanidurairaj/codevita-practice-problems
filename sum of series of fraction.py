i/p:3
explanation:1/1+1/2+1/3
o/p:11/6
1.83






a=int(input("Enter the number: "))
c=0
d=1
for i in range(1,a+1):
    d=d*i
for i in range(1,a+1):
    c+=d//i
i=1
while(i<=a):
    if(c%i==0 and d%i==0):
        c=c//i
        d=d//i
        i=1
    i=i+1
print(f'{c}/{d}')
print(f'{c/d:.2f}')
