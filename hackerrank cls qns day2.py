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

