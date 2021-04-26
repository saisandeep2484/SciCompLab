print("**********************q1********************")
import math
def f(x):
    return math.exp(x)



def q1_i():
    x0 = 0
    x1 = 0.5
    x = 0.25
    l0 = (x-x1)/(x0-x1)
    a0 = f(x0)*l0
    l1 = (x-x0)/(x1-x0)
    a1 = f(x1)*l1
    return a0 + a1

def q1_ii():
    x0 = 0.5
    x1 = 1
    x = 0.75
    l0 = (x-x1)/(x0-x1)
    a0 = f(x0)*l0
    l1 = (x-x0)/(x1-x0)
    a1 = f(x1)*l1
    return a0 + a1

def q1_iii():
    x0 = 0
    x1 = 1
    x2 = 2
    x = 0.25
    l0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
    a0 = f(x0)*l0
    l1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    a1 = f(x1)*l1
    l2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))
    a2 = f(x2)*l2
    ans1 = a0 + a1 + a2
    x = 0.75
    l0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
    a0 = f(x0)*l0
    l1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
    a1 = f(x1)*l1
    l2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))
    a2 = f(x2)*l2
    ans2 = a0 + a1 + a2
    return (ans1,ans2) 


ans1 = q1_i()
print("f(0.25) using linear Lagrange interpolation =",ans1)
err1 = abs(ans1-f(0.25))
print("Error b/w approximate and actual value at 0.25 (Linear):",err1)
print("")


ans2 = q1_ii()
print("f(0.75) using linear Lagrange interpolation =",ans2)
err2 = abs(ans2-f(0.75))
print("Error b/w approximate and actual value at 0.75 (Linear):",err2)
print("")

ans3 = q1_iii()[0]
print("f(0.25) using second Lagrange interpolation =",ans3)
err3 = abs(ans3-f(0.25))
print("Error b/w approximate and actual value at 0.25 (Second):",err3)
print("")

ans4 = q1_iii()[1]
print("f(0.75) using second Lagrange interpolation =",ans4)
err4 = abs(ans4-f(0.75))
print("Error b/w approximate and actual value at 0.75 (Second):",err4)
print("")



