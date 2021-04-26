import math
import random
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x*x*x + 0.01*random.random()
    

def comp_trapezoidal(f,a,b,n):
    h = (b-a)/n
    summ = 0
    for j in range(0,n+1):
        xj = a+j*h
        if j==0 or j==n:
            summ+=h*f(xj)/2
        else:
            summ+=h*f(xj)
    return summ

xx = []
for i in range(30,3000):
    xx.append(abs(0.25-(comp_trapezoidal(f1,0,1,i))))
    

plt.title("Error vs n")
plt.xlabel("n")
plt.ylabel("error")
plt.plot(range(30,3000),xx)
plt.xticks(range(30,3000,500))
plt.show()
