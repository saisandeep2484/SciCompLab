import math

def fa(x,m=1):
    return x/(x*x+1)

def fb(x,m=1):
    return 1/(1-x)

def fc(x,m):
    denom = math.sqrt(1-m*(math.sin(x))*(math.sin(x)))
    return 1/denom
    
used = {}

def comp_trapezoidal(f,a,b,n,m=1):
    h = (b-a)/n
    summ = 0
    cn=0
    for j in range(0,n+1):
        xj = a+j*h
        if j==0 or j==n:
            if xj in used:
                summ+=h*used[xj]/2
            else:
                cn+=1
                used[xj] = f(xj,m) 
                summ+=h*used[xj]/2
        else:
            if xj in used:
                summ+=h*used[xj]
            else:
                cn+=1
                used[xj] = f(xj,m) 
                summ+=h*used[xj]
    return summ,cn


def driver(f,a,b,err,m=1):
    used.clear()
    n = 1
    ans = -1
    cnt = 1
    function_calls = 0
    while 1:
        Th,c1 = comp_trapezoidal(f,a,b,n,m)
        Th_by_2,c2 = comp_trapezoidal(f,a,b,2*n,m)
        function_calls+=c1+c2
        val = abs(Th-Th_by_2)/abs(Th_by_2)
        print('{:.10f}'.format((b-a)/(2*n)),'{:.10f}'.format(Th_by_2),'{:.10f}'.format(val))
        if val<err:
            ans = Th_by_2
            return ans,cnt,function_calls
        
        n = n*2
        cnt+=1



print("Part (a)")
print("Table:")
print("")
print("      h    ","    T(h/2)    ","Error value")

(ans,ct,calls) = driver(fa,0,3,pow(10,-6))

print("")
print("Estimated value:",ans)
print("Number of iterations taken :",ct)
print("Number of fucntion calls :",calls)

print("Diffirence between actual and estimated value :",abs(ans-1/2*math.log(10)))

print("")
print("Part (b)")
print("Table:")
print("")
print("      h    ","    T(h/2)    ","Error value")

(ans,ct,calls) = driver(fb,0,0.95,pow(10,-6))

print("")
print("Estimated value:",ans)
print("Number of iterations taken :",ct)
print("Number of fucntion calls :",calls)

print("Diffirence between actual and estimated value :",abs(ans - math.log(20)))

print("Part (c)")
for m in [0.5,0.8,0.95]:
    print("")
    print("For m = ",m)
    print("Table:")
    print("")
    print("      h    ","    T(h/2)    ","Error value")

    (ans,ct,calls) = driver(fc,0,math.pi/2,pow(10,-6),m)

    print("")
    print("Estimated value:",ans)
    print("Number of iterations taken :",ct)
    print("Number of fucntion calls :",calls)

    



