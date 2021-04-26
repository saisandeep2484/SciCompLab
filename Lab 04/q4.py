import math
import numpy as np
import matplotlib.pyplot as plt

def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
    
        denom = (x1-x2) * (x1-x3) * (x2-x3);
        A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom;
        B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom;
        C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom;
        return A,B,C

def f1(x):
    return 1/(x+2)

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def trapezoidal(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))

def simpsons(f,a,b):
    return (1/3)*trapezoidal(f,a,b) + (2/3)*midpoint(f,a,b)

print("The actual value of the Integral =",1.09861228866811)



xx = np.linspace(-1,1,400)
yy = 1/(xx+2)

plt.plot(xx,yy)
plt.fill_between(xx,yy,alpha=.2,label='Actual')

xx1 = np.array([-1,1])
yy1 = 1/(xx1+2)

print("The estimate using trapezoidal method: ",trapezoidal(f1,-1,1))
plt.plot(xx1,yy1)
plt.fill_between(xx1,yy1,alpha=.2,label='Trapezoidal')
plt.title("Actual vs Trapezoidal")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

a,b,c = calc_parabola_vertex(-1,f1(-1),0,f1(0),1,f1(1))
xx2 = xx
yy2 = a*(xx)*(xx) + b*(xx) + c

plt.plot(xx,yy)
plt.fill_between(xx,yy,alpha=.2,label='Actual')

print("The estimate using simpon's method: ",simpsons(f1,-1,1))
plt.plot(xx2,yy2)
plt.fill_between(xx2,yy2,alpha=.2,label='Simpsons')
plt.legend()
plt.title("Actual vs Simpsons")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

        

    
