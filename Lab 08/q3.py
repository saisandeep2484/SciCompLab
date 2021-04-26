import numpy as np
import math
from prettytable import PrettyTable

def y(x):
    return 2*math.exp(x) - x -1

def r(x):
    return 1

def p(x):
    return -1

def q(x):
    return 0

def fdm(h,a,b,alpha,beta):
    
    n = (int)((b-a)/h)
    
    x = []
    x.append(a);
    for i in range(1,n+1):
        x.append(x[-1]+h)
        
#     print(n,x)
    def A(i):
        return 1 - h*p(x[i])/2
    
    def B(i):
        return -2 + h*h*q(x[i])
    
    def C(i):
        return 1 + h*p(x[i])/2
    
    L = np.zeros([n-1,n-1])
    F = np.zeros([n-1,1])
    
    for i in range (0,n-1):
        a_pos = i-1;
        b_pos = i;
        c_pos = i+1;
        if a_pos>=0 and a_pos<=n-2:
            L[i][a_pos] = A(i+1);
        if b_pos>=0 and b_pos<=n-2:
            L[i][b_pos] = B(i+1);
        if c_pos>=0 and c_pos<=n-2:
            L[i][c_pos] = C(i+1);
            
    for i in range(0,n-1):
        if i==0:
            F[i] = h*h*r(x[i+1])-alpha*(1 - h*p(x[i+1])/2)
        elif i==n-2:
            F[i] = h*h*r(x[i+1])-beta*(1 + h*p(x[i+1])/2)
        else:
            F[i] = h*h*r(x[i+1])
            
    L_inv = np.linalg.inv(L)
    U = np.dot(L_inv,F)
    
    return U

print("h = 1/3")
tab = PrettyTable()
tab.field_names = ["xi", "y(xi)", "FDM approximation", "Error"]
u = fdm(1/3,0,1,1,2*math.exp(1)-2)
tab.add_row([0,1,1,0]);
cn = 0;
for xx in [1/3,2/3]:
    tab.add_row([xx,y(xx),u[cn][0],abs(y(xx)-u[cn][0])])
    cn+=1
tab.add_row([1,2*math.exp(1)-2,2*math.exp(1)-2,0]);
print(tab)




        
        
        
        
    
    
    