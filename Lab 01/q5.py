# -*- coding: utf-8 -*-
from __future__ import division
import math
print("")
print("-------------q5-------------")
print("")


def f(x):
    return (math.exp(-x)*(x*x +5*x +2) + 1)

def SecantMethod():
    print("Method Used : Secant Method")
    x0 = -1
    x1 = 0
    root = x0
    n = 0
    while 1:
        n+=1
        if(f(x1)==f(x0)):
            root = x2
            break
        x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
        #print(x0,x1,x2)
        if abs(x1-x0) <= x1*pow(10,-5):
            root = x2
            break
        else:
            x0 = x1
            x1 = x2
        
    print("Approximate root found:",root)
    print("Number of iterations taken :",n)
         
    

SecantMethod()