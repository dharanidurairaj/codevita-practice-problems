#Watson gives four 3-dimensional points to Sherlock and asks him if they all lie in the same plane. Your task here is to help Sherlock.

Input Format
First line contains T, the number of testcases.
Each test case consists of four lines. Each line contains three integers, denoting xi yi zi.

Output Format
For each test case, print YES or NO whether all four points lie in same plane or not, respectively.

Constraints
1 ≤ T ≤ 104
-103 ≤ xi,yi,zi ≤ 103

Sample Input

1
1 2 0
2 3 0
4 0 0
0 0 0
Sample Output

YES
Explanation
All points have zi = 0, hence they lie in the same plane, and output is YES#


------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------






t = int(input())
for j in range(t):
    x = []
    y = []
    z = []
    for i in range(4):
        a,b,c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    x.sort()
    y.sort()
    z.sort()
    print (["NO", "YES"][x[3]-x[0]==0 or y[3]-y[0]==0 or z[3]-z[0]==0])
    
    
    
    -----------------------------------------------------------------------------------------------------------------------
    -----------------------------------------------------------------------------------------------------------------------

    
    
    a=int(input())
for i in range(0,a):
    x,y,z=map(int,input().split())
    x1,y1,z1=map(int,input().split())
    x2,y2,z2=map(int,input().split())
    x3,y3,z3=map(int,input().split())
    if(x1==x==x2==x3 or y1==y==y2==y3 or z1==z==z2==z3):
        print("YES")
    else:
        print("NO")
