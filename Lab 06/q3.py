import math


def func_main(x,y):
    chad = (1/(x*x))-(y/(x))-(y*y)
    return chad

def func_eval(x):
    return (-1/x)

def laghelp(xvector,fvector,storm):
    ll=len(xvector)-1
    sum=0
    for j in range(ll+1):
        prod=1
        x=xvector[j]
        y=fvector[j]
        mod1=[]
        mod2=[]
        for kk in range(ll+1):
            mod1.append(xvector[kk])
            mod2.append(fvector[kk])
        mod1.pop(j)
        mod2.pop(j)
        for i in range(ll):
            prod=prod*((storm-mod1[i])/(x-mod1[i]))
        prod=prod*y
        sum+=prod
    return sum

def euler_func(h,a,b,y0):
    n = int((b-a)/h)
    y = [0]*(n+1);x = [0]*(n+1);
    y[0] = y0
    for i in range(0,n+1):
        x[i]=a+h*i
    
    print("Number of nodes:",n+1)
        
    for i in range(1,n+1):
        y[i]=y[i-1]+func_main(x[i-1],y[i-1])*h
        
    for i in range(0,n+1):
        print("******************")
        print("At x =",round(x[i],2),", the estimated value of y is :",round(y[i],6))
        print("At x =",round(x[i],2),", the actual value of y is :",round(func_eval(x[i]),6))
        print("At x =",round(x[i],2),", the error value is :",abs(round(y[i]-func_eval(x[i]),6))) 
        
    return x,y

print("Part (a)")

xx,yy = euler_func(0.05,1,2,-1)

ans = [0]*3

cn = 0
for ele in [1.052,1.555,1.978]:
    ans[cn] = laghelp(xx,yy,ele)
    cn+=1
    
# print(ans)
print("")
print("Part (b)")

cn = 0
for val_x in [1.052,1.555,1.978]:
    print("***********************")
    print("The value of x :",val_x)
    est = ans[cn]
    cn+=1
    print("The estimated value of y is (Interpolation):",round(est,6))
    print("The actual value of y:",func_eval(val_x))
    print("The error between them is:",round(abs(func_eval(val_x)-est),6))



    
    
    
    
    
    
    
    