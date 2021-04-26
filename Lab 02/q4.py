print("**********************q4********************")
import math

def f(x):
    if x==1.0:
        return 0.1924
    if x==1.05:
        return 0.2414
    if x==1.10:
        return 0.2933
    if x==1.15:
        return 0.3492
    return 0

def f_actual(x):
    return math.log(math.tan(x),10)


def q4():
    x0 = 1.0
    x1 = 1.05
    x2 = 1.1
    x3 = 1.15
    print("x0 =",x0)
    print("x1 =",x1)
    print("x2 =",x2)
    print("x3 =",x3)
    a0 = f(x0)/((x0-x1)*(x0-x2)*(x0-x3))
    a0 = round(a0,4)
    summ = x1 + x2 + x3
    two_sum = x1*x2 + x2*x3 + x3*x1 
    product =  x1*x2*x3
    b0 = -a0*summ
    c0 = a0*two_sum
    d0 = -a0*product
    b0 = round(b0,4);c0 = round(c0,4);d0 = round(d0,4)
    a1 = f(x1)/((x1-x0)*(x1-x2)*(x1-x3))
    a1 = round(a1,4)
    summ = x0 + x2 + x3
    two_sum = x0*x2 + x2*x3 + x3*x0 
    product =  x0*x2*x3
    b1 = -a1*summ
    c1 = a1*two_sum
    d1 = -a1*product
    b1 = round(b1,4);c1 = round(c1,4);d1 = round(d1,4)
    a2 = f(x2)/((x2-x0)*(x2-x1)*(x2-x3))
    a2 = round(a2,4)
    summ = x1 + x0 + x3
    two_sum = x0*x1 + x0*x3 + x3*x1 
    product =  x0*x1*x3
    b2 = -a2*summ
    c2 = a2*two_sum
    d2 = -a2*product
    b2 = round(b2,4);c2 = round(c2,4);d2 = round(d2,4)
    a3 = f(x3)/((x3-x0)*(x3-x1)*(x3-x2))
    a3 = round(a3,4)
    summ = x1 + x0 + x2
    two_sum = x0*x1 + x0*x2 + x2*x1 
    product =  x0*x1*x2
    b3 = -a3*summ
    c3 = a3*two_sum
    d3 = -a3*product
    b3 = round(b3,4);c3 = round(c3,4);d3 = round(d3,4)
    return a0 + a1 + a2 + a3,b0 + b1 + b2 + b3,c0 + c1 + c2 + c3,d0 + d1 + d2 + d3

a3,a2,a1,a0 = q4()
a3 = round(a3,4)
a2 = round(a2,4)
a1 = round(a1,4)
a0 = round(a0,4)

print("P(x) = ",a3,"x^3 + ",a2,"x^2 + ",a1,"x + ",a0,sep="")

val = a3*1.09*1.09*1.09+a2*1.09*1.09 + a1*1.09 + a0
print("P(1.09) =","{0:.4f}".format(val))
print("f(1.09) =","{0:.4f}".format(f_actual(1.09)))

error = abs(val-f_actual(1.09))

print("Error b/w actual and calculated values:","{0:.4f}".format(error))



