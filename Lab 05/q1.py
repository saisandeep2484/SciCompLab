import math
import numpy as np
import scipy.integrate as integrate

def f1(y):
    return (1/4)*((y+5)/4)*((y+5)/4)*math.log((y+5)/4)

def f2(y):
    return (0.35)/(((0.35*y+0.35)/2)*(((0.35*y+0.35)/2)) - 4)

def f3(y):
    pp = math.pi
    return (y+1)*(y+1)*(pp/8)*(pp/8)*(pp/8)*math.sin(pp*(y+1)/8)

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
#     for i in range(0,len(nodes)):
#         nodes[i] = round(nodes[i],10)
    
    weights = [0]*(n+1)    
    for j in range(0,n+1):
        lj = lambda a : l(nodes,j,a)
        weights[j] = integrate.quad(lj, low_lim, up_lim)[0]
        
    
    fin_ans = 0
    for i in range(0,len(weights)):
        fin_ans+=weights[i]*f(nodes[i])
    
    return fin_ans


print("Part (a)")
ans = (func(f1,2,-1,1))
print("Estimated Value (with n = 2):",ans)  
Actual_val = 0.192259357732796
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")

print("Part (b)")
ans = (func(f2,2,-1,1))
print("Estimated Value (with n = 2):",ans)  
Actual_val = -0.176820020121789
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")

print("Part (c)")
ans = (func(f3,2,-1,1))
print("Estimated Value (with n = 2):",ans)  
Actual_val = 0.08875528443525664
print("Actual Value of Integral:",Actual_val)
print("Error in the estimation:",abs(Actual_val-ans))
print("")
