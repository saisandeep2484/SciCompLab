import math

def f1(x):
    if x==0:
        return 1.101
    if x==-0.25:
        return 0.33493750
    if x==-0.5:
        return -0.02475000
    if x==-0.75:
        return -0.07181250
    
def f2(x):
    if x==0.1:
        return -0.62049958
    if x==0.2:
        return -0.28398668
    if x==0.3:
        return 0.00660095
    if x==0.4:
        return 0.24842440
    

def delta(ind,x,pw,f):
    if pw==0:
        return f(x[ind])
    return delta(ind+1,x,pw-1,f)-delta(ind,x,pw-1,f)
        
def calc(x,f,order,x_est):
    h = abs(x[1]-x[0])
    ans = 0
    v = (x_est-x[-1])/h
    pro = 1
    for i in range(0,order+1):
        ans+=pro*delta(order-i,x,i,f)
        pro*=(v+i)/(i+1)
    return ans;

print("Part1")

print("Nodes Used :",[-0.5,-0.25])
print("Using Interpolating polynomial of degree 1, estimate at x = -1/3 :" ,round(calc([-0.5,-0.25],f1,1,-1/3),6))
print("Nodes Used :",[-0.75,-0.5,-0.25])
print("Using Interpolating polynomial of degree 2, estimate at x = -1/3 :" ,round(calc([-0.75,-0.5,-0.25],f1,2,-1/3),6))
print("Nodes Used :",[-0.75,-0.5,-0.25,0])
print("Using Interpolating polynomial of degree 3, estimate at x = -1/3 :" ,round(calc([-0.75,-0.5,-0.25,0],f1,3,-1/3),6))

print("")

print("Part2")

print("Nodes Used :",[0.2,0.3])
print("Using Interpolating polynomial of degree 1, estimate at x = 0.25 :",round(calc([0.2,0.3],f2,1,0.25),6))
print("Nodes Used :",[0.1,0.2,0.3])
print("Using Interpolating polynomial of degree 2, estimate at x = 0.25 :",round(calc([0.1,0.2,0.3],f2,2,0.25),6))
print("Nodes Used :",[0.1,0.2,0.3,0.4])
print("Using Interpolating polynomial of degree 3, estimate at x = 0.25 :",round(calc([0.1,0.2,0.3,0.4],f2,3,0.25),6))