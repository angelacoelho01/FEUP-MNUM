import math

def f(x):
    return math.exp(x - 2)/x


def trapezoidal(xi, xf, h):
    n = round((xf - xi)/h)
    
    print("h = " + str(h) + ", n = " + str(n))
    
    y0 = f(xi)
    yn = f(xf)
    area = 0
    
    for i in range(1, n):
        area += f(xi + i*h)
        
    return (h/2) * (y0 + yn + 2*area)


def simpson(xi, xf, h):
    n = round((xf - xi)/h)
    
    print("h = " + str(h) + ", n = " + str(n))

    y0 = f(xi)
    yn = f(xf)   
    area = 0
    
    for i in range(1, n):
        if i%2 == 0:
            area += 2 * f(xi + i*h)
        else:
            area += 4 * f(xi + i*h)
            
    return (h/3) * (y0 + yn + area)
    
    

def convergenceQuotient(xi, xf, h, rule):
    S = rule(xi, xf, h)
    print("\tS = " + str(S), '\n')

    S_l = rule(xi, xf, h/2)
    print("\tS' = " + str(S_l), '\n')
    
    S_ll = rule(xi, xf, h/4)
    print("\tS'' = " + str(S_ll), '\n')

    qc = (S_l - S)/(S_ll - S_l)
    
    print("QC = " + str(qc), '\n')
    
    return qc
    
xi = 1
xf = 5
h = 1

print("---------------Trapezoial rule---------------", '\n')
convergenceQuotient(xi, xf, h, trapezoidal)
print("---------------------------------------------", '\n\n')

print("---------------Simpson's rule----------------", '\n')
convergenceQuotient(xi, xf, h, simpson)
print("---------------------------------------------", '\n\n')

    

