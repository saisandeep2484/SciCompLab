import math


#q1
# print('lol')
def RK_fourth(h, k1,k2,k3,k4,y):
    return y + (1/6)*h*(k1+(2*k2)+(2*k3)+k4)

def f(x):
    return 6.22*(10**-19)*(((2*(10**3))-(x/2))**4)*(((3*(10**3))-(3*x/4))**3)

y1=RK_fourth(0.05,f(0),f(0.025),f(0.025),f(0.05),0)
y2=RK_fourth(0.05,f(0.05),f(0.075),f(0.075),f(0.1),y1)
y3=RK_fourth(0.05,f(0.1),f(0.125),f(0.125),f(0.15),y2)
y4=RK_fourth(0.05,f(0.15),f(0.175),f(0.175),f(0.2),y3)

print('Using fourth order method Range-Kutta , Units of KOH after 0.2s is : ',y4)
print('\n')


#q2
def f(x,y):
    return -y+x+1

#RK_2 order
print('Second Order Range-Kutta method : ')
for h in [0.1,0.2,0.25,0.5]:
    y=[]
    y_0=1
    x_0=0
    for i in range(0,int(1/h)):
        y1=y_0 + (h)*(f(x_0+(h/2),y_0+((h/2)*f(x_0,y_0))))
        # y.append(y1)
        print('For h = ',h,' and x = ',round(x_0+h,2),' y',i+1,' =',y1)
        y_0=y1
        x_0+=h
    print('\n')

print('Modified Euler method : ')
for h in [0.1,0.2,0.25,0.5]:
    y=[]
    y_0=1
    x_0=0
    for i in range(0,int(1/h)):
        y1=y_0 + (h/2)*(f(x_0,y_0)+f(x_0+h,y_0+(h*f(x_0,y_0))))
        # y.append(y1)
        print('For h = ',h,' and x = ',round(x_0+h,2),' y',i+1,' =',y1)
        y_0=y1
        x_0+=h
    print('\n')

# q3
def f(x,y):
    return (1+x)/(1+y)

print('Modified Euler Method :')
for h in [0.5]:
    # y=[]
    y_0=2
    x_0=1
    for i in range(0,int(1/h)):
        y1=y_0 + (h/2)*(f(x_0,y_0)+f(x_0+h,y_0+(h*f(x_0,y_0))))
        # y.append(y1)
        print('For h = ',h,' and x = ',round(x_0+h,2),' y',i+1,' =',y1)
        y_0=y1
        x_0+=h
        actual_val=math.sqrt(2*x_0+6+x_0**2)-1
        print('Actual value at t = ',x_0,' is: ',actual_val)
    print('\n')

def f(x,y):
    return (math.sin(2*x)-2*x*y)/(x**2)

for h in [0.25]:
    # y=[]
    y_0=2
    x_0=1
    for i in range(0,int(1/h)):
        y1=y_0 + (h/2)*(f(x_0,y_0)+f(x_0+h,y_0+(h*f(x_0,y_0))))
        # y.append(y1)
        print('For h = ',h,' and x = ',round(x_0+h,2),' y',i+1,' =',y1)
        y_0=y1
        x_0+=h
        actual_val=(4+math.cos(2)-math.cos(2*x_0))/(2*(x_0**2))
        print('Actual value at t = ',x_0,' is: ',actual_val)
    print('\n')

#q4
def f(x,y):
    return y -(x**2) +1

common=[0.1,0.2,0.3,0.4,0.5]

print('Runge-Kutta Second Order Method')
for h in [0.05]:
    y_RK_S=[]
    y_0=0.5
    x_0=0
    for i in range(0,2*int(1/h)):
        y1=y_0 + (h/2)*(f(x_0,y_0)+f(x_0+h,y_0+(h*f(x_0,y_0))))
        if (x_0 in common):
            y_RK_S.append(y_0)
        # print('For h = ',h,' and x = ',round(x_0+h,2),' y',i+1,' =',y1)
        y_0=y1
        x_0+=h
        x_0=round(x_0,2)
    print(y_RK_S)
    print('\n')

def RK_fourth(h, k1,k2,k3,k4,y):
    return y + (1/6)*h*(k1+(2*k2)+(2*k3)+k4)

print('Runge-Kutta Fourth Order Method')
for h in [0.1]:
    y_RK_F=[]
    y_0=0.5
    x_0=0
    for i in range(0,2*int(1/h)):
        k1=f(x_0,y_0)
        k2=f(x_0+(h/2),y_0+(0.5*k1*h))
        k3=f(x_0+(h/2),y_0+(0.5*k2*h))
        k4=f(x_0+(h),y_0+(k3*h))
        y1=RK_fourth(h,k1,k2,k3,k4,y_0)
        if (x_0 in common):
            y_RK_F.append(y_0)
        # print('For h = ',h,' and x = ',round(x_0+h,2),' y',i+1,' =',y1)
        y_0=y1
        x_0+=h
        x_0=round(x_0,2)
    print(y_RK_F)
    print('\n')

print('Euler`s Method')
for h in [0.025]:
    y_E=[]
    y_0=0.5
    x_0=0
    for i in range(0,2*int(1/h)):
        y1=y_0 + h*f(x_0,y_0)
        if (x_0 in common):
            y_E.append(y_0)
            # print(x_0)
        # print('For h = ',h,' and x = ',round(x_0+h,2),' y',i+1,' =',y1)
        y_0=y1
        x_0+=h
        x_0=round(x_0,3)
    print(y_E)
    print('\n')
