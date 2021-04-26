import math
from sympy import *

def P(x0):
    x = Symbol('x')
    Px = 3 - 2*(x+1) +0 *(x+1)*x + (x+1)*x*(x-1)
    return Px.subs(x,x0)

def Q(x0):
    x = Symbol('x')
    Qx = -1 + 4*(x+2) -3 *(x+1)*(x+2) + (x+2)*x*(x+1)
    return Qx.subs(x,x0)

print("P(-2) =",P(-2))
print("P(-1) =",P(-1))
print("P(0) =",P(0))
print("P(1) =",P(1))
print("P(2) =",P(2))

print("")
print("Q(-2) =",Q(-2))
print("Q(-1) =",Q(-1))
print("Q(0) =",Q(0))
print("Q(1) =",Q(1))
print("Q(2) =",Q(2))