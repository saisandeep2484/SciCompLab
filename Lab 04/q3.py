import math

def f1(x):
    return 1/(x*x + 9*(1-x)*(1-x))

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def trapezoidal(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))

def simpsons(f,a,b):
    return (1/3)*trapezoidal(f,a,b) + (2/3)*midpoint(f,a,b)

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

def comp_simpsons(f,a,b,n):
    h = (b-a)/n
    ans = f(a)
    for j in range(2,math.floor(n/2) + 1):
        ans+=2*f(a+(2*j-2)*h)
        
    for j in range(1,math.floor(n/2) + 1):
        ans+=4*f(a+(2*j-1)*h)
        
    ans+=f(b)
    return (h/3)*ans

print("Firstly, x was substituted by t/(1-t) to reduce the range to 0 to 1")
print("The estimate using compsoite trapezoidal method: ",comp_trapezoidal(f1,0,1,4))
print("The estimate using compsoite simpon's method: ",comp_simpsons(f1,0,1,4))

print("The Actual value of the integral :",math.pi/6)