import math
import numpy as np
import scipy.integrate as integrate

def f1(y):
    pp = math.pi
    val = (pp/2*y + pp/2)/2
    return (pp/4)*(math.cos(val)*math.log(math.sin(val)))/(1+math.sin(val)*math.sin(val))


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


for n in [1,2,3,4,5]:
    ans = func(f1,n,-1,1)
    ans = round(ans,3)
    print("Estimated Value through Gaussian Quadrature ( n = ",n,"):",ans)  
    Actual_val = -0.915
    print("Actual Value of Integral:",Actual_val)
    print("Error in the estimation:",round(abs(Actual_val-ans),2))
    print("")

