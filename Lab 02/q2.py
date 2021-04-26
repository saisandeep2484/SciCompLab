print("**********************q2********************")
import math

def f(x):
    if x==8.1:
        return 16.94410
    if x==8.3:
        return 17.56492
    if x==8.6:
        return 18.50515
    if x==8.7:
        return 18.82091
    return 0

def g(x):
    if x==-0.75:
        return -0.07181250
    if x==-0.5:
        return -0.02475000
    if x==-0.25:
        return 0.33493750
    if x==0:
        return 1.10100000
    return 0

def q2ii_degree1():
    x0 = -0.5
    x1 = -0.25
    print("x0 =",x0)
    print("x1 =",x1)
    x = -1/3
    l0 = (x-x1)/(x0-x1)
    a0 = g(x0)*l0
    l1 = (x-x0)/(x1-x0)
    a1 = g(x1)*l1
    return a0 + a1

def q2ii_degree2():
    x0 = -0.75
    x1 = -0.5
    x2 = -0.25
    print("x0 =",x0)
    print("x1 =",x1)
    print("x2 =",x2)
    x = -1/3
    l0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
    a0 = g(x0)*l0
    l1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    a1 = g(x1)*l1
    l2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))
    a2 = g(x2)*l2
    return a0 + a1 + a2

def q2ii_degree3():
    x0 = -0.75
    x1 = -0.5
    x2 = -0.25
    x3 = 0
    print("x0 =",x0)
    print("x1 =",x1)
    print("x2 =",x2)
    print("x3 =",x3)
    x = -1/3
    l0 = ((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))
    a0 = g(x0)*l0
    l1 = ((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))
    a1 = g(x1)*l1
    l2 = ((x-x0)*(x-x1)*(x-x3))/((x2-x0)*(x2-x1)*(x2-x3))
    a2 = g(x2)*l2
    l3 = ((x-x0)*(x-x1)*(x-x2))/((x3-x0)*(x3-x1)*(x3-x2))
    a3 = g(x3)*l3
    return a0 + a1 + a2 + a3

def q2i_degree1():
    x0 = 8.3
    x1 = 8.6
    print("x0 =",x0)
    print("x1 =",x1)
    x = 8.4
    l0 = (x-x1)/(x0-x1)
    a0 = f(x0)*l0
    l1 = (x-x0)/(x1-x0)
    a1 = f(x1)*l1
    return a0 + a1

def q2i_degree2():
    x0 = 8.1
    x1 = 8.3
    x2 = 8.6
    print("x0 =",x0)
    print("x1 =",x1)
    print("x2 =",x2)
    x = 8.4
    l0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
    a0 = f(x0)*l0
    l1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    a1 = f(x1)*l1
    l2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))
    a2 = f(x2)*l2
    return a0 + a1 + a2

def q2i_degree3():
    x0 = 8.1
    x1 = 8.3
    x2 = 8.6
    x3 = 8.7
    print("x0 =",x0)
    print("x1 =",x1)
    print("x2 =",x2)
    print("x3 =",x3)
    x = 8.4
    l0 = ((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))
    a0 = f(x0)*l0
    l1 = ((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))
    a1 = f(x1)*l1
    l2 = ((x-x0)*(x-x1)*(x-x3))/((x2-x0)*(x2-x1)*(x2-x3))
    a2 = f(x2)*l2
    l3 = ((x-x0)*(x-x1)*(x-x2))/((x3-x0)*(x3-x1)*(x3-x2))
    a3 = f(x3)*l3
    return a0 + a1 + a2 + a3


print("f(8.4) using linear Lagrange interpolation =",q2i_degree1())
print("")
print("f(8.4) using second Lagrange interpolation =",q2i_degree2())
print("")
print("f(8.4) using third Lagrange interpolation =",q2i_degree3())
print("")

print("f(-1/3) using linear Lagrange interpolation =",q2ii_degree1())
print("")
print("f(-1/3) using second Lagrange interpolation =",q2ii_degree2())
print("")
print("f(-1/3) using third Lagrange interpolation =",q2ii_degree3())
print("")






