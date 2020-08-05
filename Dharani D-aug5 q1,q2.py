

program 2:


Task
You are given a string .
Your task is to print all possible permutations of size of the string in lexicographic sorted order.
Input Format
A single line containing the space separated string and the integer value .
Constraints
The string contains only UPPERCASE characters.
Output Format
Print the permutations of the string on separate lines.
Sample Input
HACK 2
Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation
All possible size permutations of the string "HACK" are printed in lexicographic sorted order.



program2:



from itertools import permutations
inp1,inp2 = input().split()
inp2 = int(inp2)
inp1= list(inp1)
inp1.sort()
for i in list(permutations(inp1,inp2)):
    print(''.join(i))
    
    
    
    
program 1:  
Given the names and grades for each student in a class of students, store them in a nested list
and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names
alphabetically and print each name on a new line.
Example
The ordered list of scores is , so the second lowest score is . There are two students with that
score: . Ordered alphabetically, the names are printed as:
alpha
beta
Input Format
The first line contains an integer, , the number of students.
The subsequent lines describe each student over lines.
- The first line contains a student's name.
- The second line contains their grade.
Constraints
There will always be one or more students having the second lowest grade.
Output Format
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple
students, order their names alphabetically and print each one on a new line.
Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
output:

Berry
Harry

    
program:
inp=int(input())
l1=[]
l2=[]
for i in range(inp):
    inp1=input()
    inp2=float(input())
    l1+=[[inp1,inp2]]
    l2+=[inp2]
a=sorted(l2)[1]
for i,j in sorted(l1):
    if j==a:
        print(i)
    
