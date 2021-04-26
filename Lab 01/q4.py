# -*- coding: utf-8 -*-
from __future__ import division
import math
print("")
print("-------------q4-------------")
print("")


def f(x):
    return (-math.sin(x)+(x/2))

def g(x):
    return ((2*math.sin(x)/x) + x - 1)

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
    
def FixedPointMethod(x_init):
    print("Method Used : Fixed Point Method")
    print("")
    print("g(x) = (2sin(x)/x) + x - 1")
    print("g(x) is continuous for all x in [pi/2,pi]")
    print("pi/2 <= g(x) <= pi for all x in [pi/2,pi]")
    print("")
    x0 = x_init #initial estimate
    print("Intial Estimate (from Bisection Method) :",x0)
    eps = 1/(pow(10,15))
    print("Epsilon : 10^(-15)")
    root = x0
    n = 0
    while 1:
        n+=1
        x1 = g(x0)
        if abs(x1-x0)<=eps:
            root = x1
            break
        else:
            x0 = x1
    print("n (number of iterations) :",n)
    print("root :",root)
    print("")
    
    x0 = x_init
    n = 0
    eps = 1/pow(10,13)
    ratio = []
    xx = [] #stores the sequence values
    xx.append(x0)
    while 1:
        #print(x0)
        n+=1
        x1 = g(x0)
        xx.append(x1)
        if x0 == root or abs(x1-x0)<=eps:
            break
        else:
            rat = -1
            if len(xx) >=3:
                r1 = xx[-3]
                r2 = xx[-2]
                r3 = xx[-1]
                num = (root-r3)/(root-r2)
                denom = (root-r2)/(root-r1)
                rat = math.log(abs(num))/math.log(abs(denom))
            if rat!=-1:
                ratio.append(rat)
            x0 = x1
            
    order = ratio[-1]
    print("It can be seen that g is a contraction with L = 0.363.")
    print("The ratio log|(xn+1 - alpha)/(xn - alpha)|/log|(xn - alpha)/(xn-1 - alpha)| was calculated at each stage.")
    print("Theoretically, the above ratio should converge to the order of convergence.")
    print("Last three calulated ratios are as follows:")
    print("{0:.5f}".format(ratio[-3]),"{0:.5f}".format(ratio[-2]),"{0:.5f}".format(ratio[-1]))
    print("The ratio converges to 1 after several iterations, and hence order of convergence = 1.")
    

approx_root = BisectionMethod()
FixedPointMethod(approx_root)