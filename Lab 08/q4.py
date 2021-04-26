import numpy as np
import math
from prettytable import PrettyTable
from matplotlib import pyplot as plt

def y(x):
    return (math.exp(10*x)-1)/(math.exp(10)-1)

def r(x):
    return 0

def p(x):
    return -10

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
            
#     print(L)
#     print(F)
            
    L_inv = np.linalg.inv(L)
    U = np.dot(L_inv,F)
    
    return U


def fdm2(h,a,b,alpha,beta):
    
    n = (int)((b-a)/h)
    
    x = []
    x.append(a);
    for i in range(1,n+1):
        x.append(x[-1]+h)
        
#     print(n,x)
    def A(i):
        return 1 - h*p(x[i])
    
    def B(i):
        return -2 + h*h*q(x[i])+h*p(x[i])
    
    def C(i):
        return 1
    
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
            F[i] = h*h*r(x[i+1])-alpha*(1 - h*p(x[i+1]))
        elif i==n-2:
            F[i] = h*h*r(x[i+1])-beta
        else:
            F[i] = h*h*r(x[i+1])
            
#     print(L)
#     print(F)
            
    L_inv = np.linalg.inv(L)
    U = np.dot(L_inv,F)
    
    return U


def fdm3(h,a,b,alpha,beta):
    
    n = (int)((b-a)/h)
    
    x = []
    x.append(a);
    for i in range(1,n+1):
        x.append(x[-1]+h)
        
#     print(n,x)
    def A(i):
        return 1
    
    def B(i):
        return -2 + h*h*q(x[i])-h*p(x[i])
    
    def C(i):
        return 1 + h*p(x[i])
    
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
            F[i] = h*h*r(x[i+1])-alpha
        elif i==n-2:
            F[i] = h*h*r(x[i+1])-beta*(1 + h*p(x[i+1]))
        else:
            F[i] = h*h*r(x[i+1])
            
#     print(L)
#     print(F)
            
    L_inv = np.linalg.inv(L)
    U = np.dot(L_inv,F)
    
    return U


x = [0,1/4,2/4,3/4,1]



print("h = 1/4, Central Difference Approximation")
tab = PrettyTable()
tab.field_names = ["xi", "y(xi)", "FDM approximation", "Error"]
u = fdm(1/4,0,1,0,1)
tab.add_row([0,0,0,0]);
cn = 0;
err = []
err.append(0)
for xx in [1/4,2/4,3/4]:
    tab.add_row([xx,y(xx),u[cn][0],abs(y(xx)-u[cn][0])])
    err.append(abs(y(xx)-u[cn][0]))
    cn+=1
    
err.append(0);
tab.add_row([1,1,1,0]);
print(tab)

plt.plot(x,err,label="Central")

print("h = 1/4, Backward Difference Approximation")
tab = PrettyTable()
tab.field_names = ["xi", "y(xi)", "FDM approximation", "Error"]
u = fdm2(1/4,0,1,0,1)
tab.add_row([0,0,0,0]);
cn = 0;
err = []
err.append(0)
for xx in [1/4,2/4,3/4]:
    tab.add_row([xx,y(xx),u[cn][0],abs(y(xx)-u[cn][0])])
    err.append(abs(y(xx)-u[cn][0]))
    cn+=1
tab.add_row([1,1,1,0]);
err.append(0);
print(tab)

plt.plot(x,err,label="Backward")

print("h = 1/4, Forward Difference Approximation")
tab = PrettyTable()
tab.field_names = ["xi", "y(xi)", "FDM approximation", "Error"]
u = fdm3(1/4,0,1,0,1)
tab.add_row([0,0,0,0]);
cn = 0;
err = []
err.append(0)
for xx in [1/4,2/4,3/4]:
    tab.add_row([xx,y(xx),u[cn][0],abs(y(xx)-u[cn][0])])
    err.append(abs(y(xx)-u[cn][0]))
    
    cn+=1
tab.add_row([1,1,1,0]);
print(tab)

err.append(0);
plt.plot(x,err,label="Forward")
plt.xlabel("x")
plt.ylabel("err")
plt.title("Comparision of Errors")
plt.legend()
plt.show()
    
    
    