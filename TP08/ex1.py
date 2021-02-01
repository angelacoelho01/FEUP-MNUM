import math

g = 10
c = 15
v = 35
t = 9
error = 0.0001

def f(m):
    return (((g*m)/c) * (1 - math.exp((-c*t)/m))) - v


def diff_f(m):
    return (2 * (1 - math.exp((-c*t)/m)))/3 - (90 * math.exp((-c*t)/m))/m

def absoluteError(val1, val2):
    return abs(val1 - val2) <= error

def bisection(a, b):
    an = a
    bn = b
    m = 0
    stopCondition = False
    no_iter = 0
    
    while not stopCondition:
        m = (an + bn)/2
        
        if (f(an) * f(m)) < 0:
            bn = m
        else:
            an = m
            
        stopCondition = absoluteError(an, bn)
        no_iter += 1
        
    print("No iteratios: " + str(no_iter), '\n')
    return m


def newton(x0):
    xn = x0
    stopCondition = False
    no_iter = 0
    
    while not stopCondition:
        if (diff_f(x0) == 0):
            print("Divergent.", '\n')
            return
        
        xn = x0 - f(x0)/diff_f(x0)
        
        stopCondition = absoluteError(x0, xn)
        
        x0 = xn
        no_iter += 1
        
    print("No iteratios: " + str(no_iter), '\n')
    return xn
    


a = 10
b = 100
print("----------Bisection method----------", '\n')
print("[a, b] = [" + str(a) + ", " + str(b) + "]", '\n')
print("\tm = " + str(bisection(a, b)), '\n')
print("------------------------------------",'\n\n')


guess = 1
print("-----------Newton method------------", '\n')
print("Guess = " + str(guess), '\n')
print("\tm = " + str(bisection(a, b)), '\n')
print("------------------------------------",'\n\n')


