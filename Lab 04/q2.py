import math

def f1(x):
    if x==1:
        return 10
    if x==1.25:
        return 8
    if x==1.5:
        return 7
    if x==1.75:
        return 6
    if x==2:
        return 5

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def trapezoidal(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))

def simpsons(f,a,b):
    return (1/3)*trapezoidal(f,a,b) + (2/3)*midpoint(f,a,b)

print("For (a) part :")
print("Using Trapezoidal Method, estimated value of the integral =",round(trapezoidal(f1,1,2),6))
print("")
print("For (b) part :")
print("Using Simpsons Method, estimated value of the integral =",round(simpsons(f1,1,2),6))

