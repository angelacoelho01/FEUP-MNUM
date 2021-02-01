import math

def f(x):
    return 2 * math.exp(-1.5*x)


def trapezoidal(xi, xf, h):
    n = round((xf - xi)/h)
    y0 = f(xi)
    yn = f(xf)
    area = 0
    
    for i in range(1, n):
        area += f(xi + i*h)
        
    return (h/2) * (y0 + yn + 2*area)


def simpson(xi, xf, h):
    h /= 2
    n = round((xf - xi)/h)
    y0 = f(xi)
    yn = f(xf)
    area_odd = 0
    area_even = 0
    
    for i in range(1, n, 2):
        area_odd += 4*f(xi + i*h)
    
    for i in range(2, n-1, 2):
        area_even += 2*f(xi + i*h)
        
    return (h/3) * (y0 + yn + area_odd + area_even)


def convergenceQuotientError(xi, xf, h, rule):
    S = rule(xi, xf, h)
    S_l = rule(xi, xf, h/2)
    S_ll = rule(xi, xf, h/4)
    
    qc = (S_l - S)/(S_ll - S_l)
    
    if rule == trapezoidal:
        div = 3
    else:
        div = 15
        
    error = (S_ll - S_l)/div
    
    print("h = " + str(h), '\n')
    
    print("\tS = " + str(S))
    print("\tS' = " + str(S_l))
    print("\tS'' = " + str(S_ll), '\n')
    
    print("\tQC = " + str(qc))
    print("\tError = " + str(error), '\n')
    
        
    return qc, error


xi = 0
xf = 0.6
h = 0.15


print("---------------Trapezoidal rule---------------", '\n')
convergenceQuotientError(xi, xf, h, trapezoidal)
print("----------------------------------------------", '\n\n')
    

print("----------------Simpson's rule----------------", '\n')
convergenceQuotientError(xi, xf, h, simpson)
print("----------------------------------------------", '\n\n')
    