import math

def f1(x):
    if x==0:
        return 1
    if x==0.25:
        return 1.64872
    if x==0.5:
        return 2.71828
    if x==0.75:
        return 4.48169
    
def f2(x):
    if x==0.1:
        return -0.29004986
    if x==0.2:
        return -0.56079734
    if x==0.3:
        return -0.81401972
    if x==0.4:
        return -1.0526302
    
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

print("Nodes Used :",[0.25,0.5])
print("Using Interpolating polynomial of degree 1, estimate at x = 0.43 :" ,round(calc([0.25,0.5],f1,1,0.43),6))
print("Nodes Used :",[0.25,0.5,0.75])
print("Using Interpolating polynomial of degree 2, estimate at x = 0.43 :" ,round(calc([0.25,0.5,0.75],f1,2,0.43),6))
print("Nodes Used :",[0,0.25,0.5,0.75])
print("Using Interpolating polynomial of degree 3, estimate at x = 0.43 :" ,round(calc([0,0.25,0.5,0.75],f1,3,0.43),6))

print("")

print("Part2")

print("Nodes Used :",[0.1,0.2])
print("Using Interpolating polynomial of degree 1, estimate at x = 0.18 :",round(calc([0.1,0.2],f2,1,0.18),6))
print("Nodes Used :",[0.1,0.2,0.3])
print("Using Interpolating polynomial of degree 2, estimate at x = 0.18 :",round(calc([0.1,0.2,0.3],f2,2,0.18),6))
print("Nodes Used :",[0.1,0.2,0.3,0.4])
print("Using Interpolating polynomial of degree 3, estimate at x = 0.18 :",round(calc([0.1,0.2,0.3,0.4],f2,3,0.18),6))