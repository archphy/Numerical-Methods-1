# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 21:08:34 2014

Proper way of implementing Bisection in a parallel way is unknown to me 
So doing it sequencially....

Known error : For sufficiently complex function I cannot impose the monotonous 
condiftio

@author: sandeep
"""


def sign(num):
    """Returns 1 if positive , 0 otherwise """
    if num > 0:
        return 1
    if num < 0:
        return 0 

def func0(x):
    return 5*x**1 - x**3 + 9*x**2   
def func1(x):
    return 5*x**10 - 9*x**6 + 89*x**2   
def func2(x):
    return x**2   

def Bisection(func,xl,xh,restrictToMonotone = True ,maxIter = 1000,error = 0.000005):
    """ Returns the acceptable root and value of function at root """
    fl = func(xl)
    fh = func(xh)   # l - low , h - high
    
    if restrictToMonotone == True:
        print "Restricted to Monotonous In Given Interval"
        if sign(fl) == sign(fh) :
            print "Bisection cannot be applied to monotonus function"
            return None , None
    
    err = xh - xl 
    for counter in range(0,maxIter):
        err = err / 2 # each time the loop runs error is halved 
        mid = xl + err # Better way to compute midpoint than to invoke a difficult func
        fm = func(mid)
#        print err , mid , fm             #DEBUG
        if err < error :
            print "Acceptable root found"
            return mid , fm 
        if sign(fl) == sign(fm): # root lies between mid and high point
            xl = mid
            fl = fm  # Reducing CPU cycles
        else:        # root lies between low and mid point
            xh = mid
            fh = fm  
            
    print "Maximum Iteration exceeded : Acceptable Root Not Found"
    return mid , fm 
        
                
                
# RUN THE FUNCTION    
def BisectionBackEnd(func , a , b ,Monotone = True ):    
    root ,value = Bisection(func , a , b ,restrictToMonotone=Monotone)
    if root != None:
        print "The root is ", root ," and the value is " ,value
    
BisectionBackEnd(func0 , -10999220 , 100450000 ,Monotone= True)



