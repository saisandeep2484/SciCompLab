# -*- coding: utf-8 -*-
from __future__ import division
import math
print("")
print("-------------q3-------------")
print("")


def f(x):
    return (-math.sin(x)+(x/2))

def Df(x):
    return (-math.cos(x)+(1/2))

def BisectionMethod():
    print("Method Used : Bisection Method")
    a = (math.pi)/2
    b = math.pi
    eps = 1/(pow(10,1)) #epsilon
    print("Epsilon : 10^(-1)")
    n = math.ceil((math.log(b-a) - math.log(eps))/math.log(2))
    print("n (number of iterations) :",n)
    while n>0:
        n = n-1
        c = (a+b)/2
        if f(b)*f(c)<=0:
            a = c
        else:
            b = c
    
    print("aprroximate root of f(x) = x/2 - sinx in the interval [pi/2,pi] :",c)
    print("")
    return c
    
def NewtonsMethod(x_init):
    print("Method Used : Newton's Method")
    x0 = x_init #initial estimate
    print("Intial Estimate (from Bisection Method) :",x0)
    eps = 1/(2*pow(10,7))
    print("Epsilon : 0.5 x 10^(-7)")
    root = x0
    n = 0
    while 1:
        n+=1
        Dfx0 = Df(x0)
        if Dfx0 == 0:
            print("First Derivative is 0")
            break
        x1 = x0 - f(x0)/Dfx0
        if abs(x1-x0) <= eps:
            root = x1
            break
        else:
            x0 = x1
    print("n (number of iterations) :",n)
    print("The root (accurate upto 7 decimal places) of f(x) = x/2 - sinx in the interval [pi/2,pi] :",root)
    print("")
    

approx_root = BisectionMethod()
NewtonsMethod(approx_root)
