import math

def f1(x):
    return 1/(x+4)

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def trapezoidal(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))

def simpsons(f,a,b):
    return (1/3)*trapezoidal(f,a,b) + (2/3)*midpoint(f,a,b)

def err_comp_trap(f,a,b,err):
    d2fmax = 1/32
    val = (1/err)*(b-a)*(b-a)*(b-a)*(1/12)*d2fmax
    n = math.ceil(math.sqrt(val))
    print("Constraints :","h <=",(b-a)/math.sqrt(val),"and n >=",n)
    return n 

def err_comp_simp(f,a,b,err):
    d4fmax = 24/(4**5)
    val = (1/err)*pow(b-a,5)*(1/180)*d4fmax
    n = math.ceil(math.sqrt(math.sqrt(val)))
    if n%2==0:
        print("Constraints :","h <=",(b-a)/math.sqrt(math.sqrt(val)),"and n >=",n)
        return n
    else:
        print("Constraints :","h <=",(b-a)/math.sqrt(math.sqrt(val)),"and n >=",n+1)
        return n+1
    
    
def err_comp_mid(f,a,b,err):
    d2fmax = 1/32
    val = (1/err)*(b-a)*(b-a)*(b-a)*(1/6)*d2fmax
    n = math.ceil(math.sqrt(val))
    print("Constraints :","h <=",(b-a)/math.sqrt(val),"and n >=",n)
    return n
    


def comp_trapezoidal(f,a,b,n):
    h = (b-a)/n
    summ = 0
    for j in range(0,n+1):
        xj = a+j*h
        if j==0 or j==n:
            summ+=h*f(xj)/2
        else:
            summ+=h*f(xj)
    return summ

def comp_simpsons(f,a,b,n):
    h = (b-a)/n
    ans = f(a)
    for j in range(2,math.floor(n/2) + 1):
        ans+=2*f(a+(2*j-2)*h)
        
    for j in range(1,math.floor(n/2) + 1):
        ans+=4*f(a+(2*j-1)*h)
        
    ans+=f(b)
    return (h/3)*ans

def comp_midpoint(f,a,b,n):
    h = (b-a)/n
    ans = 0
    summ = 0
    for j in range(0,n):
        xj = a+j*h
        xj_nex = a+(j+1)*h
        pt = (xj+xj_nex)/2
        summ+=f(pt)
    return h*summ
    

actual_val = 0.405465108108164

print("Part (a)")
req_n = err_comp_trap(f1,0,2,pow(10,-5))
req_h = (2-0)/req_n


print("Required value of n:",req_n)
print("Correpsonding value of h:",req_h)

ans = comp_trapezoidal(f1,0,2,req_n)
print("The estimate using compsoite trapezoidal method: ",ans)
print("The diffirence between actual and caluclated value:",abs(ans-actual_val))

print("")
print("Part (b)")
req_n = err_comp_simp(f1,0,2,pow(10,-5))
req_h = (2-0)/req_n


print("Required value of n:",req_n)
print("Correpsonding value of h:",req_h)

ans1 = comp_simpsons(f1,0,2,req_n)
print("The estimate using compsoite simpsons method: ",ans1)
print("The diffirence between actual and caluclated value:",abs(ans1-actual_val))

print("")
print("Part (c)")
req_n = err_comp_mid(f1,0,2,pow(10,-5))
req_h = (2-0)/req_n


print("Required value of n:",req_n)
print("Correpsonding value of h:",req_h)

ans1 = comp_midpoint(f1,0,2,req_n)
print("The estimate using compsoite midpoint method: ",ans1)
print("The diffirence between actual and caluclated value:",abs(ans1-actual_val))