import math
import numpy as np
import scipy.integrate as integrate


def Simpson_one_third(a,b,h):
    n=int((b-a)/h)
    ans=(1/(1+a))+(1/(1+b))
    for i in range(2,n,2):
        ans+=2*(1/(1+a+i*h))
    for i in range(1,n,2):
        ans+=4*(1/(1+a+i*h))
    ans*=h
    ans/=3
    return ans


def f1(y):
    return 1/(2*((y+1)/2 + 1))

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
    # for i in range(0,len(nodes)):
    #     nodes[i] = round(nodes[i],10)
    
    weights = [0]*(n+1)    
    for j in range(0,n+1):
        lj = lambda a : l(nodes,j,a)
        weights[j] = integrate.quad(lj, low_lim, up_lim)[0]
        
    
    fin_ans = 0
    for i in range(0,len(weights)):
        fin_ans+=weights[i]*f(nodes[i])
    
    return fin_ans



ans = func(f1,2,-1,1)
print("Estimated Value through Gaussian Quadrature (three-point):",ans)  
Actual_val = 0.6931471805599453
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")


ans = Simpson_one_third(0,1,0.125)
print("Estimated Value through Simpson's 1/3 rule:",ans)  
Actual_val = 0.6931471805599453
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")


