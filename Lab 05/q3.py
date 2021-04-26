import math
import numpy as np
import scipy.integrate as integrate

def f1(x):
    return 1/(x+2)

def l(x_arr,j,x_point):
        ans = 1
        for i in range(0,len(x_arr)):
            if i==j:
                continue
            ans *=(x_point-x_arr[i])/(x_arr[j]-x_arr[i])
        return ans
    

def func(f,n,low_lim,up_lim):
    # we require roots of legendre polynomial of degree n+1
    coeff_arr = [0]*(n+2)
    coeff_arr[-1] = 1
    nodes = np.polynomial.legendre.legroots(coeff_arr)
    for i in range(0,len(nodes)):
        nodes[i] = round(nodes[i],10)
    
    weights = [0]*(n+1)    
    for j in range(0,n+1):
        lj = lambda a : l(nodes,j,a)
        weights[j] = integrate.quad(lj, low_lim, up_lim)[0]
        
    
    fin_ans = 0
    for i in range(0,len(weights)):
        fin_ans+=weights[i]*f(nodes[i])
    
    return fin_ans



ans = func(f1,1,-1,1)
print("Estimated Value through Gaussian Quadrature (two-point):",ans)  
Actual_val = 1.09861228866811
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def trapezoidal(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))

def simpsons(f,a,b):
    return (1/3)*trapezoidal(f,a,b) + (2/3)*midpoint(f,a,b)

ans = trapezoidal(f1,-1,1)
print("Estimated Value through Trapezoidal rule:",ans)  
Actual_val = 1.09861228866811
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")


ans = simpsons(f1,-1,1)
print("Estimated Value through Simpson's rule:",ans)  
Actual_val = 1.09861228866811
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")





