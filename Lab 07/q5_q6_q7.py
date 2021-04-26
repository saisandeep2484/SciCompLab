from math import *
import matplotlib.pyplot as plt
import numpy as np

def print_ques(n):
    s = f'Question {n}'
    print('\n'+ s + '\n'+ '='*len(s))

def rungekutta4(f, x0, x, h, y0, all=False):
    yi = y0
    N = int(round((x - x0)/h))
    ys = [y0]
    for i in range(1, N+1):
        xi = i*h + x0
        k1 = f(xi, yi)
        k2 = f(xi + h/2, yi + h*k1/2)
        k3 = f(xi + h/2, yi + h*k2/2)
        k4 = f(xi + h, yi + h*k3)
        yi = yi + h*(k1 + 2*k2 + 2*k3 + k4)/6
        ys.append(yi)
    if all:
        return ys
    else:
        return yi

def rungekutta2(f, x0, x, h, y0, all = False):
    yi = y0
    N = int(round((x - x0)/h))
    ys = [y0]
    for i in range(1, N+1):
        xi = i*h + x0
        yi = yi + h*f(xi + h/2, yi + h*f(xi, yi)/2)
        ys.append(yi)
    if all:
        return ys
    return yi

def modified_euler(f, x0, x, h, y0, all=False):
    yi = y0
    N = int(round((x - x0)/h))
    res = [y0]
    for i in range(1, N+1):
        xi = i*h + x0
        yi = yi + h*((1/2)*(f(xi, yi) + f(xi + h, yi + h*f(xi, yi))))
        res.append(yi)
    if all:
        return res
    else:
        return res[-1]

def ques4():
    print_ques(4)
    h = 0.025
    f = lambda t, y: y - t**2 + 1
    x0 = 0; y0 = 0.5
    eu = euler(f, x0, y0, h, 20)[::4]
    h = 0.05
    r2 = rungekutta2(f, x0, x0+h*10, h, y0, all=True)[::2]
    h = 0.1
    r4 = rungekutta4(f, x0, x0+h*5, h, y0, all=True)
    for i in range(0, 6):
        print(f'x={x0+i*h:.4f} \t euler={eu[i]} \t rungekutta2={r2[i]} rungekutta4={r4[i]}')


def adambash(f, x0, h, n, y0, y1, y2, y3):
    ys = [0]*(n+1)
    xs = [x0+i*h for i in range(n+1)]
    ys[0], ys[1], ys[2], ys[3] = y0, y1, y2, y3
    for i in range(3, n):
        ys[i+1] = ys[i] + (h/24)*(55*f(xs[i], ys[i]) - 59*f(xs[i-1], ys[i-1]) + 37*f(xs[i-2], ys[i-2]) - 9*f(xs[i-3], ys[i-3]))
    return ys

def adammoult(f, x0, h, n, ys):
    ys = list(ys)
    def f1(i):
        return f(x0 + i*h, ys[i])

    for i in range(2, len(ys)-1):
        ys[i+1] = ys[i] + (h/24)*(9*f1(i+1) + 19*f1(i) - 5*f1(i-1) + f1(i-2))    
    return ys

def ques5():
    print_ques(5)
    h = 0.2
    t0 = 0
    def y(t):
        return (t+1)**2 - 0.5*np.exp(t)
    def f(t, y):
        return y - t**2 + 1

    iniys = [y(t0+i*h) for i in range(11)]

    # bashforth four step method
    bashys = adambash(f, t0, h, 10, *iniys[:4])

    # moutlo
    moultys = adammoult(f, t0, h, 10, iniys)

    print(f' adam-bash\t  adam-mltn \t differ \t initial ys \t')
    # print( '-------------------------------------------------------')
    for i in range(len(bashys)):
        a, b, c = bashys[i], moultys[i], iniys[i]
        d = abs(b - a)
        print(f' {a:.9f} \t {b:.9f} \t {d:.9f}  {c:.9f} \t')


    # print(f'bash    = {bashys}')
    # print(f'moutlys = {moultys}')
    # print(f'iniys   = {iniys}')


def ques6():
    print_ques(6)
    N = 10
    head = '\n     x \t  Act.  \t   Comp \t   Diff \t'

    # (a)
    # y(0) = 1, h = 0.1  ; actual y(t) = (2*t + 1)/(t**2 + 1)

    f = lambda t, y: (2 - 2*t*y)/(t**2 + 1)
    act = lambda t:  (2*t + 1)/(t**2 + 1)
    x0 = 0; y0 = 1; h = 0.1

    xs = np.array([x0 + i*h for i in range(N+1)])
    iniys = rungekutta4(f, x0, x0 + 4*h, h, y0, all = True)
    res = adambash(f, x0, h, N, *iniys[:4])
    print(head)
    # print('-----------------------------------------------------------------------')
    for i in range(N):
        print(f' {xs[i]:.5f} \t {act(xs[i]):.5f} \t {res[i]:.5f} \t {abs(act(xs[i]) - res[i]):.5f} \t')


    # (b)
    f = lambda t, y: (y**2)/(t + 1)
    act = lambda t:  -1/np.log(t+1)
    x0 = 1; y0 = -1/np.log(2); h = 0.1

    xs = np.array([x0 + i*h for i in range(N+1)])
    iniys = rungekutta4(f, x0, x0 + 4*h, h, y0, all = True)
    res = adambash(f, x0, h, N, *iniys[:4])
    print(head)
    # print('-----------------------------------------------------------------------')
    for i in range(N):
        print(f' {xs[i]:.5f} \t {act(xs[i]):.5f} \t {res[i]:.5f} \t {abs(act(xs[i]) - res[i]):.5f} \t')

    # (c)
    f = lambda t, y: (y**2 + y)/t
    act = lambda t:  2*t/(1-t)
    x0 = 1; y0 = -2; h = 0.2

    xs = np.array([x0 + i*h for i in range(N+1)])
    iniys = rungekutta4(f, x0, x0 + 4*h, h, y0, all = True)
    res = adambash(f, x0, h, N, *iniys[:4])
    print(head)
    # print('-----------------------------------------------------------------------')
    for i in range(1,N):
        print(f' {xs[i]:.5f} \t {act(xs[i]):.5f} \t {res[i]:.5f} \t {abs(act(xs[i]) - res[i]):.5f} \t')



def ques7():
    print_ques(7)
    
    f = lambda t, y:   y - t**2 + 1
    # y(0) = 0.5
    h = 0.2; x0 = 0; y0 = 0.5; n = 10
    iniys = rungekutta4(f, x0, x0+4*h, h, y0, all=True)[:3]
    predys = adambash(f, x0, h, n, y0, *iniys)
    corrys = adammoult(f, x0, h, n, predys)

    for i in range(len(corrys)):
        print(f'x = {x0 + i*h:.3f} \t calculated \t f(x) = {corrys[i]}')




ques5()
ques6()
ques7()