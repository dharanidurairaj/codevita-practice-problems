i/p:abcdefghwxyz
o/p:ABCD efgh WXYZ



a=input()
d=a.partition("efgh")
print(d[0].upper(),end=" ")
print(d[1],end=" ")
print(d[2].upper(),end=" ")

