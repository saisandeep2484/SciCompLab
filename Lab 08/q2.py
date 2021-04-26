import numpy as np
import math
from math import sin
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def y(x):
    return sin(x)



def p(x):
    return 0

def q(x):
    return 0

def fdm(n,a,b,alpha,beta):
    h = ((b-a)/n)
    x = []
    x.append(a);
    for i in range(1,n+1):
        x.append(x[-1]+h)
        
#     print(n,x)
    def A(i):
        return 1
    
    def B(i):
        return -2
    
    def C(i):
        return 1
    
    def r(i):
        return -sin(x[i])-(1/12)*(sin(x[i-1])-2*sin(x[i]) + sin(x[i+1])) 
    
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
            F[i] = h*h*r(i+1)
        elif i==n-2:
            F[i] = h*h*r(i+1)
        else:
            F[i] = h*h*r(i+1)
            
    L_inv = np.linalg.inv(L)
    U = np.dot(L_inv,F)
    
    return U


def maxnorm(calc, real):
    mx = 0
    arg = 0
    
    for i in range(len(calc)):
        if abs(calc[i] - real[i]) > mx:
            mx = abs(calc[i] - real[i])
            arg = i
    return arg, mx

def l2norm(calc, real):
    calc = np.array(calc)
    real = np.array(real)
    return np.sqrt(np.sum((calc-real)**2)/np.size(calc))

Ns = [10,20,40,80,160,320]
l2errors = []
maxerrors = []
for n in Ns:
    print("n = ", n,", Central Diffirence Approximation")
    tab = PrettyTable()
    tab.field_names = ["xi", "y(xi)", "FDM approximation", "Error"]
    U = fdm(n,0,2*math.pi,0,0)
    tab.add_row([0,0,0,0]);
    cn = 0;
    for xxx in range(1,n):
        xx = (xxx*math.pi*2)/n

        tab.add_row([round(xx,12),round(y(xx),12),round(U[cn][0],12),round(abs(y(xx)-U[cn][0]),12)])
        cn+=1
    tab.add_row([round(2*math.pi,12),0,0,0]);
    print(tab)
    U = [np.sin(0)] + list(np.array(U).ravel()) + [np.sin(2*math.pi)]
    real = [np.sin(i*2*np.pi/n) for i in range(len(U))]
    
    l2errors.append(l2norm(U, real))
    maxerrors.append(maxnorm(U, real)[1])

plt.plot(Ns, l2errors, 'x-', label='$L^2$ norm')
plt.plot(Ns, maxerrors, 'x-', label='Maximum norm')

l2m, _ = np.polyfit(np.log(np.array(Ns)), np.log(np.array(l2errors)), 1)
maxm, _ = np.polyfit(np.log(np.array(Ns)), np.log(np.array(maxerrors)), 1)

print(f'Slope L2 norm: {l2m}\nSlope max norm : {maxm}')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()
plt.show()