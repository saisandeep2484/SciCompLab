import math
from sympy import *

def func():
    x = Symbol('x')
    Px = x*(x-1)*(x-2) + x*(x-1)*(x-2)*(x-3)
    Px = simplify(Px)
    Px = expand(Px)
    ans = Px.subs(x,12)-2*Px.subs(x,11)+Px.subs(x,10)
    return ans

print("The value of (delta^2)P(10) =",func())