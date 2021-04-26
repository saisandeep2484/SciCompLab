import math


def func2(typ,x):
    if typ ==1:
        chad = math.log(math.exp(x)+math.exp(1)-1)
    if typ ==2:
        chad = -1+math.sqrt(x*x+2*x+6)
    if typ ==3:
        chad = (x-2+math.sqrt(2)*math.exp(1-0.5*x))
        chad = chad*chad
    if typ ==4:
        chad =  (4+math.cos(2)-math.cos(2*x))/(2*x*x)
    return chad


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
        print("At x =",x[i],", the error value is :",abs(round(y[i]-func2(typ,x[i]),6)))
        
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



    
    
    
    
    
    
    
    