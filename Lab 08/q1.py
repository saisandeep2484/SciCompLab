import numpy as np
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def y(x):
    return 1 + x - math.cos(x) -(1+math.pi/2)*math.sin(x)

def r(x):
    return 1+x

def p(x):
    return 0

def q(x):
    return 1

def fdm(h,a,b,alpha,beta,x_req,met):
    
    n = (int)((b-a)/h)
    
    x = []
    x.append(a);
    for i in range(1,n+1):
        x.append(x[-1]+h)
        
#     print(n,x)
    def a(i):
        return 1 - h*p(x[i])/2
    
    def b(i):
        return -2 + h*h*q(x[i])
    
    def c(i):
        return 1 + h*p(x[i])/2
    
    L = np.zeros([n-1,n-1])
    F = np.zeros([n-1,1])
    
    for i in range (0,n-1):
        a_pos = i-1;
        b_pos = i;
        c_pos = i+1;
        if a_pos>=0 and a_pos<=n-2:
            L[i][a_pos] = a(i+1);
        if b_pos>=0 and b_pos<=n-2:
            L[i][b_pos] = b(i+1);
        if c_pos>=0 and c_pos<=n-2:
            L[i][c_pos] = c(i+1);
            
    for i in range(0,n-1):
        if i==0:
            F[i] = h*h*r(x[i+1])-alpha*(1 - h*p(x[i+1])/2)
        elif i==n-2:
            F[i] = h*h*r(x[i+1])-beta*(1 + h*p(x[i+1])/2)
        else:
            F[i] = h*h*r(x[i+1])
            
    L_inv = np.linalg.inv(L)
    U = np.dot(L_inv,F)
    if met==0:
        return U
    
    cn = int(n/2 -1)
    return U[cn][0]




tab = PrettyTable();
tab.field_names = ["h","y(pi/4)","f.d. solution at pi/4","error","Ratio of Error (ei-1/ei)"]

prev_err = -1;
for xx in [4,8,16,32,64]:
    h = math.pi/xx
    curr_val = '-'
    if prev_err!=-1:
        curr_val =  abs(fdm(h,0,math.pi/2,0,0,math.pi/4,1)-y(math.pi/4))/prev_err
    tab.add_row([h,y(math.pi/4),fdm(h,0,math.pi/2,0,0,math.pi/4,1),abs(fdm(h,0,math.pi/2,0,0,math.pi/4,1)-y(math.pi/4)),curr_val])
    prev_err = abs(fdm(h,0,math.pi/2,0,0,math.pi/4,1)-y(math.pi/4))
    
print(tab)

h = math.pi/64
a = 0
b = math.pi/2
n = (int)((b-a)/h)
x = []
x.append(a);
for i in range(1,n+1):
    x.append(x[-1]+h)
    
y1 = []

for ele in x:
    y1.append(y(ele));

u = fdm(h,0,math.pi/2,0,0,math.pi/4,0)


y2 = []
y2.append(y(a));
for cn in range(1,n):
    y2.append(u[cn-1][0])
    
y2.append(y(b));

# print(y1)
# print(y2)
plt.plot(x,y1,c='r',label="Actual")
plt.plot(x,y2,c='g',label="FDM Estimated")
plt.ylabel("Actual and Estimated value of Y")
plt.xlabel('x')
plt.title("y versus x for h = pi/64 (estimated and actual)")
plt.legend()
plt.show()


plt.scatter(x[6:7],y1[6:7],c='r',label="Actual")
plt.scatter(x[6:7],y2[6:7],c='g',label="FDM Estimated")
plt.ylabel("Magnified difference between both points")
plt.xlabel('x')
plt.title("Magnified difference between both points at x = 3pi/32")
plt.legend()
plt.show()
        
    
    
    