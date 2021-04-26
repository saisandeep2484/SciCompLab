import math
import numpy as np
import matplotlib.pyplot as plt

print("**********************q5(Newton)********************")

def sel_n(lst, n): 
    if n == 0: 
        return [[]] 
    l =[] 
    for i in range(0, len(lst)): 
          
        m = lst[i] 
        remLst = lst[i + 1:] 
          
        for p in sel_n(remLst, n-1): 
            l.append([m]+p)        
    return l 

def calc(lst):
    ans = 0
    for arr in lst:
        pro = 1
        for ele in arr:
            pro*=ele
        ans+=pro
    return ans

def f(x):
    return math.erf(x)
    

def N(j,inp,x):
    if j == 0:
        return 1
    ans = 1
    for k in range(0,j):
        ans *= (inp-x[k])
    return ans
        
    
def q5_Newton(x,y):
    n = len(x)
    mat = np.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            if i>=j:
                mat[i][j] = N(j,x[i],x)
    
    A_inv = np.linalg.inv(mat)
    vec_y = np.zeros(shape=(n,1))
    for i in range(0,n):
        vec_y[i][0] = y[i]
    res = np.dot(A_inv,vec_y)
    
    a = []
    for i in range(0,len(res)):
        a.append(res[i][0])
    # a[i] for x^i 
    c = [0]*n
    for i in range(n-1,-1,-1):
        fact = a[i]
        c[i]+=fact
        cn = 0
        for j in range(i-1,-1,-1):
            lst = sel_n(x[:i],cn+1)
            if cn%2==1:
                c[j] += fact*calc(lst)
            else:
                c[j] -= fact*calc(lst)
            cn+=1
                
    c = np.flipud(c) 
    ans = ""
    for i in range(0,len(c)):
        coef = round(c[i],6)
        if(coef>=0 and i>=1):
            if i==n-1:
                st = "+" + str(coef)
            else:
                st = "+" + str(coef)+"x^"+str(n-i-1)+ " "
        else:
            if i==n-1:
                st = str(coef)
            else:
                st = str(coef)+"x^"+str(n-i-1)+ " "
        ans+=st
    return c,ans


def calc_val(c,x0):
    ans = 0
    for i in range(0,len(c)):
        ans+=c[i]*math.pow(x0,len(c)-1-i)
    return ans
    
x = np.linspace(1,3,11)
y = [f(xx) for xx in x]
c,ans = q5_Newton(x,y)
print("Newton Interpolation Polynomial is: ")
print("L(x) =",ans)

xx = np.linspace(0,4,401)

yy = []
for ele in xx:
    actual = f(ele)
    calculated = calc_val(c,ele)
    yy.append(abs(actual-calculated))
    
plt.plot(xx, yy)
plt.xlabel("x")
plt.ylabel("Error")
plt.xticks(np.linspace(0,4,11))
plt.title("Error for erf function (Newton Method)")
plt.grid(True)
plt.show()
    


            
        