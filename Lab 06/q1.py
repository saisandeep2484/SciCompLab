import math

def func(typ,x,y):
    if typ ==1:
        chad = math.exp(x-y)
    if typ ==2:
        chad = (1+x)/(1+y)
    if typ ==3:
        chad = (-y+x*math.sqrt(y))
    if typ ==4:
        chad = pow(x,-2)*(math.sin(2*x)-2*x*y)
    return chad

def euler_func(typ,h,a,b,y0):
    n = int((b-a)/h)
    y = [0]*(n+1);x = [0]*(n+1);
    y[0] = y0
    for i in range(0,n+1):
        x[i]=a+h*i
    
    print("Number of nodes:",n+1)
        
    for i in range(1,n+1):
        y[i]=y[i-1]+func(typ,x[i-1],y[i-1])*h
        
    for i in range(0,n+1):
        print("At x =",x[i],", the estimated value of y is :",round(y[i],6))
        
    return y


print("Part (a)")
euler_func(1,0.5,0,1,1)

print("")
print("Part (b)")
euler_func(2,0.5,1,2,2)

print("")
print("Part (c)")
euler_func(3,0.25,2,3,2)

print("")
print("Part (d)")
euler_func(4,0.25,1,2,2)



    
    
    
    
    
    
    
    