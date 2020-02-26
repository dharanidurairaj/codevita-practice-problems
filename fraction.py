i/p:
5
o/p:
137/60
2.28






from fractions import Fraction
a=int(input("Enter the number: "))
l=[]
c=0
for i in range(1,a+1):
    l.append(Fraction(1,i))
    c=c+(1/i)
print(sum(l))
print(round(c,2))
