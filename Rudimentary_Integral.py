# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 20:27:31 2014

@author: sandeep
"""

#function used for everything
def function(x):
    return x**3 - 0.165*x**2 + 3.993*10**(-4)
#program to compute the left riemann sum .... 

def xfrange(start, stop, step):
    while start < stop:
        yield start
        start += step
    
def getBase(x_0,x_n,numberOfRects):
    return (x_n - x_0) / numberOfRects
    
def getHeight(x):
    return fn(x)
    
def fn(x):
    return x**2

def takeIntegral(function,x_0,x_1,n):
    base = getBase(x_0,x_1,n)
    integral = 0 
    for x in xfrange(x_0,x_1,base):
        integral += base * fn(x)
    print integral 
       
print '\n'
print 'Take intergral'         
takeIntegral(function,0,0.11,2)