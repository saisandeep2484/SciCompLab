# -*- coding: utf-8 -*-
from __future__ import division
import math
print("")
print("-------------q2-------------")
print("")


def f(x):
    return (math.tan(math.pi-x)-x)



def func(n):
    a = 1.6
    b = 3
    h = (b-a)/n
    ans = abs(f(a)-0)
    root = a
    for i in range(1,n+1):
        x = a + i*h
        ans1 = abs(f(x)-0)
        if ans1<ans:
            ans = ans1
            root = x
            
    
    print("For n =",n,", the root obtained is =",root)
    
func(1)
func(5)
func(20)
func(100)
func(200)
func(400)
func(1000)
func(10000)
func(50000)