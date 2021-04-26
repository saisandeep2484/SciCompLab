import math
import numpy as np
import matplotlib.pyplot as plt

print("**********************q5(Lagrange)********************")

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
    

def q5_Lagrange(x,y):
    n = len(x)
    c = [0]*n
    for i in range(0,n):
        phi_xi = 1
        for j in range(0,n):
            if j!=i:
                phi_xi*=(x[i]-x[j])
        c[0] += y[i]/phi_xi
        a0 = y[i]/phi_xi
        elem = x[i]
        x = np.delete(x, i)
        for j in range(1,n):
            lst = sel_n(x,j)
            if j%2==0:
                c[j] += a0*calc(lst)
            else:
                c[j] -= a0*calc(lst)
                
        x = np.insert(x,i,elem)  
    
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
c,ans = q5_Lagrange(x,y)
print("Lagrange Interpolation Polynomial is: ")
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
plt.title("Error for erf function (Lagrange Method)")
plt.grid(True)
plt.show()
    


            
        