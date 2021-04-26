import math
import numpy as np
import matplotlib.pyplot as plt

print("**********************q5(Monomial)********************")

def f(x):
    return math.erf(x)
    

def q5_Monomial(x,y):
    n = len(x)
    mat = np.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            mat[i][j] = math.pow(x[i],j)
    
    A_inv = np.linalg.inv(mat)
    vec_y = np.zeros(shape=(n,1))
    for i in range(0,n):
        vec_y[i][0] = y[i]
    res = np.dot(A_inv,vec_y)
    c = []
    for i in range(0,len(res)):
        c.append(res[i][0])
        
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
c,ans = q5_Monomial(x,y)
print("Monomial Interpolation Polynomial is: ")
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
plt.title("Error for erf function (Monomial Method)")
plt.grid(True)
plt.show()
    


            
        