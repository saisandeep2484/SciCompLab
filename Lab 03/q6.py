import math
from sympy import *

def f(x):
    if x==0:
        return 4
    if x==1:
        return 9
    if x==2:
        return 15
    if x==3:
        return 18
    
def delta(ind,x,pw,f):
    if pw==4:
        return 1
    if pw==0:
        return f(x[ind])
    return delta(ind+1,x,pw-1,f)-delta(ind,x,pw-1,f)
        
def calc(x_arr,f,order):
    x = Symbol('x')
    ans = 0*x + delta(0,x_arr,0,f)
    pro = x
    for i in range(1,order+1):
        ans+=pro*delta(0,x_arr,i,f)
        pro*=(x-i)/(i+1)
    
    ans = simplify(ans)
    return ans

x = Symbol('x')
a = Poly(calc([0,1,2,3],f,4),x)

print("P(x) = ",calc([0,1,2,3],f,4))
print("The coefficient of x^3 is",a.coeffs()[1])
