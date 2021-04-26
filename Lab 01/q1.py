# -*- coding: utf-8 -*-
from __future__ import division
print("")
print("-------------q1-------------")
print("")

a = 2
curr_ele = 10 #current element (xn)
next_ele = (curr_ele*(curr_ele*curr_ele + 3*a))/(3*curr_ele*curr_ele + a) #next element (xn+1)

print("Starting element chosen is : x1 = ",curr_ele)

tol = 1/pow(10,5) #epsilon


count = 1

while 1:
    if abs(next_ele-curr_ele) <= tol:
        break
    count+=1
    next_next_ele = (next_ele*(next_ele*next_ele + 3*a))/(3*next_ele*next_ele + a) #next of next element
    curr_ele = next_ele
    next_ele = next_next_ele
    
print("Number of iterations such that |xn+1 - xn| <= 10^(-5) is :",count)



order = 1
alpha = 1.4143


curr_ele = 10
next_ele = (curr_ele*(curr_ele*curr_ele + 3*a))/(3*curr_ele*curr_ele + a)
C = abs(alpha-next_ele)/abs(alpha-curr_ele)

count = 0
while 1:
    #print(C)
    if count > 100:
        break
    count+=1
    next_next_ele = (next_ele*(next_ele*next_ele + 3*a))/(3*next_ele*next_ele + a) # next of next element
    curr_ele = next_ele
    next_ele = next_next_ele
    C = abs(alpha-next_ele)/abs(alpha-curr_ele)
    
print("By assuming the order to be 1, the ratio (aplha - xn+1)/(alpha-xn) was calculated at each step.")
print("After several iterations, the ratio appeared to converge to a certain fixed value.")
print("Hence, the order is 1")