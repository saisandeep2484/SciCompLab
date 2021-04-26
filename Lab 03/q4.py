import math

def gx(x):
    if x==0.1:
        return 9.9833
    if x==0.2:
        return 4.9667
    if x==0.3:
        return 3.2836
    if x==0.4:
        return 2.4339
    if x==0.5:
        return 1.9177
    
def xgx(x):
    if x==0.1:
        return x*9.9833
    if x==0.2:
        return x*4.9667
    if x==0.3:
        return x*3.2836
    if x==0.4:
        return x*2.4339
    if x==0.5:
        return x*1.9177
    
    
def delta(ind,x,pw,f):
    if pw==0:
        return f(x[ind])
    return delta(ind+1,x,pw-1,f)-delta(ind,x,pw-1,f)
        
def calc(x,f,order,x_est):
    h = abs(x[1]-x[0])
    ans = 0
    u = (x_est-x[0])/h
    pro = 1
    for i in range(0,order+1):
        ans+=pro*delta(0,x,i,f)
        pro*=(u-i)/(i+1)
        
    return ans;

print("Part1")
act = math.sin(0.25)/(0.25*0.25)
ans1 = calc([0.1,0.2,0.3,0.4,0.5],gx,4,0.25)
print("Using direct g(x), estimate at x = 0.25 :" ,round(ans1,6))
print("Error =",abs(ans1-act))
print("")

print("Part2")
ans2 = 4*calc([0.1,0.2,0.3,0.4,0.5],xgx,4,0.25)
print("Using xg(x), estimate at x = 0.25 :",round(ans2,6))
print("Error =",abs(ans2-act))

print("")

