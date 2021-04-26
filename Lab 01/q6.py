# -*- coding: utf-8 -*-
from __future__ import division
import math
print("")
print("-------------q6-------------")
print("")


def f(x):
    return math.exp(-x)*(x*x + 5*x + 2) + 1

def BisectionMethod():
    print("Method Used : Bisection Method")
    a = -1
    b = 0
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
    
    print("aprroximate root of f(x) in the interval [-1,0] :",c)
    print("")
    return c
    
def iterativeMethod(x_init):
    print("Method Used : Iterative Method (as per Question)")
    x0 = x_init #initial estimate
    print("x0 (from Bisection Method) :",x0)
    x_cur = x0+1
    eps = 1/(pow(10,15))
    print("Epsilon : 10^(-15)")
    root = x0
    n = 0
    while 1:
        n+=1
        x_next = (x0*f(x_cur) - x_cur*f(x0))/(f(x_cur)-f(x0))
        if abs(x_next-x_cur)<=eps:
            root = x_next
            break
        else:
            x_cur = x_next
    print("n (number of iterations) :",n)
    print("root :",root)
    print("")
    
    x0 = x_init
    x_cur = x0+1
    n = 0
    eps = 1/pow(10,13)
    ratio = []
    xx = [] #stores the sequence values
    xx.append(x0)
    xx.append(x_cur)
    while 1:
        n+=1
        x_next = (x0*f(x_cur) - x_cur*f(x0))/(f(x_cur)-f(x0))
        xx.append(x_next)
        if abs(x_next-x_cur)<=eps:
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
            x_cur = x_next
            
    order = ratio[-1]
    print("The ratio log|(xn+1 - alpha)/(xn - alpha)|/log|(xn - alpha)/(xn-1 - alpha)| was calculated at each stage.")
    print("Theoretically, the above ratio should converge to the order of convergence.")
    print("Last three calulated ratios are as follows:")
    print("{0:.5f}".format(ratio[-3]),"{0:.5f}".format(ratio[-2]),"{0:.5f}".format(ratio[-1]))
    print("The ratio converges to 1 after several iterations, and hence order of convergence = 1.")
    
    

approx_root = BisectionMethod()
iterativeMethod(approx_root)
