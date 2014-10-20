# -*- coding: utf-8 -*-
"""
Created on Sat Sep 06 13:16:15 2014

@author: sandeep
"""

from __future__ import division
import math

##################################################################
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

def takeIntegral(fn,x_0,x_1,n):
    base = getBase(x_0,x_1,n)
    integral = 0 
    for x in xfrange(x_0,x_1,base):
        integral += base * fn(x)
    print integral        
print '\n'
print 'Take intergral'         
takeIntegral(function,0,0.11,2)

#########################################################
# COnverting interger into binary 


#Skipping 

#########################################################
#Bisection method or Binary Search Method 

# Finds the zero of a fucntion given two guess . 
""" Algorithm 
 
 Obtain two guess xh and xl
 Take mid of xl and xh 
 STEP
 check 
 if f(xl) == 0 :
     return xl as zero 
 if f(xh) == 0 :
     return xh as zero 
 if f(xm) == 0 :
     return xm as zero 
 if f(xl)*f(xm) < 0:
     recursively apply with xl = xl and xh = xm 
 if f(xl)*f(xm) > 0 :
      recursively apply with xl = xm and xh = xh
 
  At each step ,when you have found the upper or lower limit ,
  find Ea = abs(xmOld -xmNew )/xmNew * 100 
  if Ea > Tolerance , 
      then go to STEP
"""

def bisectionRoot(f,xl,xh,count=100000,toleranceInPercent=0.0001):
    '''Guaratee of convergence '''
    counter = 0 
    #print "debug"
    while (counter < count):
         counter += 1 
         xm = (xl + xh)/2
         if f(xl) == 0 :
             return xl #as zero
         if f(xh) == 0 :
             return xh #as zero 
         if f(xm) == 0 :
             return xm#as zero 
         if f(xl)*f(xm) < 0:
             xl = xl 
             xh = xm
         if f(xh)*f(xm) < 0 :
            # print 4 
             xh = xh 
             xl = xm
         if counter != 1 :
             if toleranceCheck(toleranceInPercent,relativeError(xm,xmOld)):
                 return xm
         xmOld = xm 
    return xm 
         
        
        
   # return bisectionUpdate(f,xl,xh,xm,toleranceInPercent)
     # recursively apply with xl = xm and xh = xh

def toleranceCheck(tolerance,value):
     # do something only if the value has a value 
    if tolerance > value : # Vlaue has to be less than tolerance 
        return True
    else:
        return False
     
def bisectionUpdate(f,xl,xh,xmOld,tolerance):
    xmNew = (xl + xh)/2
    if f(xl) == 0 :
      #  print 1
        return xl #as zero
    if f(xh) == 0 :
       # print 2
        return xh #as zero 
    if f(xmNew) == 0 :
        #print 3
        return xmNew #as zero 
    if f(xl)*f(xmNew) < 0:
       # print 3
        return bisectionUpdate(f,xl,xmNew,xmNew,tolerance) #recursively apply with xl = xl and xh = xm 
    if f(xh)*f(xmNew) < 0 :
        #print 4 
        return bisectionUpdate(f,xmNew,xh,xmNew,tolerance)
    if toleranceCheck(tolerance,relativeError(xmOld,xmNew)):
        return xmNew 
    else:
       # print 5
        return 0
        
    
    
def relativeError(new,old=None):
    if(old ==None or new ==None):
        return 10000 
    else:
        return abs(new - old )/new * 100 
print '\n'
#print relativeError(0.1)
print 'bisectioRoot : '
print bisectionRoot(function,0,0.11)    


print '\n'
print 'Netwon Raphson Method :' 
"""
guess = xi -f(xi)/f'(xi)

f'(xi) =
Approximate via the central divided derivative 

"""
def centralDividedDerivative(f,x):
    delta = 0.000001
    fh = f(x+delta)
    fl = f(x-delta)
    width =2*delta
    
    return ((fh-fl)/width)
    
#print centralDividedDerivative(function,1)   
 
def NewtonRaphason(f,guess = .11,count=10000,tolerance = .0001):# implementing Tolerance is better 
    #Finds the zero of the given function 
    '''No guarantee of convergence as no bracketing , local method '''
    counter = 0 
        
    while ( (counter < count)):
        counter+=1 
        newGuess = guess - (f(guess)/centralDividedDerivative(f,guess))
        guess = newGuess
        check = toleranceCheck(tolerance, relativeError(newGuess,guess))
        if check:
            break
    return newGuess 
    
print NewtonRaphason(function,2)


#print 'Divide without Division Operator '
def division(num,denom):
    '''Division is expensive so compute the inverse and then multiply 
    use equation x = 1/denom and when we find the value of x , we just 
    have to multiply......
    On solving the Eqn for NR method 
    
    newGuess = guess(1 + denom*guess)
     
    division 25 clock cycles approx
    multiplication 5 clock 
    add / sub 2 
    
    '''
    #initialize the guess with small numbers ..........
    guess = 0.1
    counter = 0 
    while(counter < 10):
        counter+=1
        newGuess =  guess*(2 - denom*guess)
        guess = newGuess
        
    return num*newGuess 

#print division(1,2.5) 

#print 'Find square root of any number by NR method'
def findSquareRoot(square): 
    '''Use the function 
       x**2 - square = 0 
       
       then use NR formula
    '''
    guess = 0.1
    counter = 0 
    while(counter < 100):
        counter+=1
        newGuess =  guess - (guess**2 - square)/(2*guess)
        guess = newGuess
           
    return newGuess
    
#print findSquareRoot(12222209)
#print '\n'
#######################################################################
#print 'Seacant Method' 
''' Simply tries to overcome the issues of finding the derivative in Newton 
Raphson method , by using a BDD ...
'''
#print 'Skipping' 
'''
Equation 
xNew = xOld - f(xOld)/(f'(xOld))

f'(xOld) approximated as : 
(f(xOld) - f(xOld - delta) ) /xOld -(xOld - delta)

No Guarantee of covergence ....
'''
print '\n'
print 'False Position Method ' 

def falsePosition(f,xl,xh,count=100000,toleranceInPercent=0.0001):
    '''Guaratee of convergence '''
    counter = 0 
    #print "debug"
    while (counter < count):     
        counter += 1 
        xm = ( xh*f(xl) - xl*f(xh) )/( f(xl) - f(xh) )
        if (f(xl) * f(xm))< 0: #root betw xl and xm
             xl = xl 
             xh = xm
        elif(f(xl) * f(xm))> 0:  # root betw xm and xh
            # print 4 
             xh = xh 
             xl = xm     
        else:
             return xm 
        if counter != 1 :
            if toleranceCheck(toleranceInPercent,relativeError(xm,xmOld)):
                 return xm
        xmOld = xm 
    return xm 
         
         
print falsePosition(function,0,0.11)

''' How to know how many significant digit , 
    it should satisfy the equation 
    realtive error <= .5*10**(2-m)
    , where m is the number of significant digits'''
