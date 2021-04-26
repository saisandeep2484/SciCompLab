import math
from sympy import *

x = Symbol('x') 
Px = 1 + 4*x + 4*x*(x-0.25) + (16/3)*(x)*(x-0.25)*(x-0.5)

print("f(0.75) =",Px.subs(x,0.75))