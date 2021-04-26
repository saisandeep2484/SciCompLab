print("**********************q3********************")
import math

def f(x):
    return math.exp(-x*x)

def q3():
    x0 = -1
    x1 = -0
    x2 = 1
    print("x0 =",x0)
    print("x1 =",x1)
    print("x2 =",x2)
    denom = f(x0)/((x0-x1)*(x0-x2))
    a0 = denom
    b0 = denom*(x1+x2)*(-1)
    c0 = denom*x1*x2
    denom = f(x1)/((x1-x0)*(x1-x2))
    a1 = denom
    b1 = denom*(x0+x2)*(-1)
    c1 = denom*x0*x2
    denom = f(x2)/((x2-x0)*(x2-x1))
    a2 = denom
    b2 = denom*(x1+x0)*(-1)
    c2 = denom*x1*x0
    return (a0+a1+a2,b0+b1+b2,c0+c1+c2)

a2,a1,a0 = q3()
print("P2(x) =",a2,"x*x + ",a1,"x + ",a0,sep="")

val = a2*0.9*0.9 + a1*0.9 + a0
print("P2(0.9) =","{0:.6f}".format(val))
print("f(0.9) =","{0:.6f}".format(f(0.9)))

error = abs(val-f(0.9))

print("Error b/w actual and calculated values:","{0:.6f}".format(error))



