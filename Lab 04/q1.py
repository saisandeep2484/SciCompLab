import math

def f1(x):
    return math.cos(x)/(1+math.cos(x)*math.cos(x))

def f2(x):
    return 1/(5+4*math.cos(x))

def f3(x):
    return math.exp(-x*x)

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def trapezoidal(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))

def simpsons(f,a,b):
    return (1/3)*trapezoidal(f,a,b) + (2/3)*midpoint(f,a,b)

print("For (a) part :")
print("Using Midpoint Method, estimated value of the integral =",round(midpoint(f1,0,math.pi/2),6))
print("Diffirence between actual and calculated value :",round(abs(0.623225-midpoint(f1,0,math.pi/2)),6))
print("Using Trapezoidal Method, estimated value of the integral =",round(trapezoidal(f1,0,math.pi/2),6))
print("Diffirence between actual and calculated value :",round(abs(0.623225-trapezoidal(f1,0,math.pi/2)),6))
print("Using Simpsons Method, estimated value of the integral =",round(simpsons(f1,0,math.pi/2),6))
print("Diffirence between actual and calculated value :",round(abs(0.623225-simpsons(f1,0,math.pi/2)),6))

print("")
print("For (b) part :")
print("Using Midpoint Method, estimated value of the integral =",round(midpoint(f2,0,math.pi),6))
print("Diffirence between actual and calculated value :",round(abs(1.047198-midpoint(f2,0,math.pi)),6))
print("Using Trapezoidal Method, estimated value of the integral =",round(trapezoidal(f2,0,math.pi),6))
print("Diffirence between actual and calculated value :",round(abs(1.047198-trapezoidal(f2,0,math.pi)),6))
print("Using Simpsons Method, estimated value of the integral =",round(simpsons(f2,0,math.pi),6))
print("Diffirence between actual and calculated value :",round(abs(1.047198-simpsons(f2,0,math.pi)),6))

print("")
print("For (c) part :")
print("Using Midpoint Method, estimated value of the integral =",round(midpoint(f3,0,1),6))
print("Diffirence between actual and calculated value :",round(abs(0.746824-midpoint(f3,0,1)),6))
print("Using Trapezoidal Method, estimated value of the integral =",round(trapezoidal(f3,0,1),6))
print("Diffirence between actual and calculated value :",round(abs(0.746824-trapezoidal(f3,0,1)),6))
print("Using Simpsons Method, estimated value of the integral =",round(simpsons(f3,0,1),6))
print("Diffirence between actual and calculated value :",round(abs(0.746824-simpsons(f3,0,1)),6))


    