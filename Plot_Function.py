# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 22:10:29 2014

Draw Back is unable to draw modulo fucntion 

@author: sandeep
"""

import numpy as np
import matplotlib.pyplot as plt

def plotFunction(f,min = -1000,max = 1000):
    print f
    x = np.arange(min, max, 0.1);
    y = f(x)
    plt.plot(x,y)



def func0(x):
    return 5*x**1 - x**3 + 9*x**2   
def func1(x):
    return 5*x**10 - 9*x**6 + 89*x**2   
def func(x):
    return x**2
def func3(x):
    return x**3
def func7(x):
    return x**7  
def func6(x):
    return x**6  
    
def modulo(x):
    if x > 0 :
        return x 
    else :
        return -x

plotFunction(func)
plt.show()
plotFunction(func1)
plt.show()
plotFunction(func0,min = -99999 ,max = 99999)
plt.show()
plotFunction(func3)
plt.show()
plotFunction(func7)
plt.show()
plotFunction(func6)
plt.show()
print "odd"
plotFunction((lambda x: x**101))
plt.show()
print "even "
plotFunction((lambda x: x**100))
plt.show()
plotFunction((lambda x: np.sin(x)),min = -6 , max = 6)
plt.show()
plotFunction((lambda x: np.cos(x)),min = -6 , max = 6)
plt.show()

plotFunction((lambda x: np.tan(x)),min = -1 , max = 1)
plt.show()
print 
plotFunction(modulo)
plt.show()
