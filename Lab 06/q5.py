import math


def func_main(x,y):
    lam = -20
    chad = lam*y + math.cos(x) - lam*math.sin(x) 
    return chad

def func_eval(x):
    return math.sin(x)


def euler_func(h,a,b,y0):
    n = int((b-a)/h)
    y = [0]*(n+1);x = [0]*(n+1);
    y[0] = y0
    for i in range(0,n+1):
        x[i]=a+h*i
    
    print("Number of nodes:",n+1)
        
    for i in range(1,n+1):
        y[i]=y[i-1]+func_main(x[i-1],y[i-1])*h
        
    print("For x =",b,", the estimated value of y is :",y[n])
    print("For x =",b,", the actual value of y is :",func_eval(x[n]))
    print("The error between actual and real value is:",abs(func_eval(x[n])-y[n]))
    
euler_func(0.5,0,3,0)

print("")
print("If we decrease the value of h to lesser values (decrease by 10 times), then:")

euler_func(0.05,0,3,0)

print("")
Y = 0.5 * 1
err = 6*0.5*0.5*Y
print("The maximum error bound is (with h = 0.5):",err)

print("The absolute error is much more than the theoretical max error.")


