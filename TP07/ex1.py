def f(x, y):
    return x**2 + y**2


def euler(x0, y0, xi, xf, h):
    n = round((xf - xi)/h)
    xn = x0
    yn = y0
    
    for i in range(0, n):
        yn = yn + (h * f(xn, yn))
        xn = xn + h
                
    return yn


def rk4(x0, y0, xi, xf, h):
    n = round((xf - xi)/h)
    xn = x0
    yn = y0
    
    for i in range(0, n):
        delta_y1 = h * f(xn, yn)
        delta_y2 = h * f(xn + h/2, yn + delta_y1/2)
        delta_y3 = h * f(xn + h/2, yn + delta_y2/2)
        delta_y4 = h * f(xn + h, yn + delta_y3)
        delta_y = delta_y1/6 + delta_y2/3 + delta_y3/3 + delta_y4/6
        
        yn = yn + delta_y
        xn = xn + h
        
    return yn


def convergenceQuotientError(x0, y0, xi, xf, h, method):
    S = method(x0, y0, xi, xf, h)
    S_l = method(x0, y0, xi, xf, h/2)
    S_ll = method(x0, y0, xi, xf, h/4)
    qc = (S_l - S)/(S_ll - S_l)
    
    if method == euler:
        div = 1
    else:
        div = 15
        
    error = (S_ll - S_l)/div
    
    print("\tS = " + str(S))
    print("\tS' = " + str(S_l))
    print("\tS'' = " + str(S_ll), '\n')
    print("\tQC = " + str(qc))
    print("\tError = " + str(error), '\n')
    
    return qc, error


x0 = 0
y0 = 0
h = 0.1
xi = 0


print("---------------Euler method---------------", '\n')
xf = 0.7
print("h = " + str(h), '\n')
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, xi, xf, h, euler)
xf = 1.4
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, xi, xf, h, euler)
print("------------------------------------------", '\n\n')


print("----------------RK4 method----------------", '\n')
xf = 0.7
print("h = " + str(h), '\n')
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, xi, xf, h, rk4)
xf = 1.4
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, xi, xf, h, rk4)
print("------------------------------------------", '\n\n')



