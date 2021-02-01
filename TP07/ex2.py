def diff_y(x, y, z):
    return z*y + x


def diff_z(x, y, z):
    return z*x + y


def euler(x0, y0, z0, xi, xf, h):
    n = round((xf - xi)/h)
    xn = x0
    yn = y0
    zn = z0
    
    for i in range(0, n):
        xn = x0 + h
        yn = y0 + h * diff_y(x0, y0, z0)
        zn = z0 + h * diff_z(x0, y0, z0)
        
        x0 = xn
        y0 = yn
        z0 = zn
        
    return yn, zn


def rk2(x0, y0, z0, xi, xf, h):
    n = round((xf - xi)/h)
    xn = x0
    yn = y0
    zn = z0
    
    for i in range(0, n):
        delta_y = diff_y(x0 + (h/2), y0 + ((h/2) * diff_y(x0, y0, z0)), z0 + ((h/2) * diff_z(x0, y0, z0)))
        delta_z = diff_z(x0 + (h/2), y0 + ((h/2) * diff_y(x0, y0, z0)), z0 + ((h/2) * diff_z(x0, y0, z0)))
        
        xn = x0 + h
        yn = y0 + h * delta_y
        zn = z0 + h * delta_z
        
        x0 = xn
        y0 = yn
        z0 = zn
        
    return yn, zn


def convergenceQuotientError(x0, y0, z0, xi, xf, h, method):
    Sy, Sz = method(x0, y0, z0, xi, xf, h)
    Sy_l, Sz_l = method(x0, y0, z0, xi, xf, h/2)
    Sy_ll, Sz_ll = method(x0, y0, z0, xi, xf, h/4)
    
    qc_y = (Sy_l - Sy)/(Sy_ll - Sy_l)
    qc_z = (Sz_l - Sz)/(Sz_ll - Sz_l)
    
    if method == euler:
        div = 1
    else:
        div = 3
        
    error_y = (Sy_ll - Sy_l)/div
    error_z = (Sz_ll - Sz_l)/div
    
    print("\tS(y) = " + str(Sy))
    print("\tS'(y) = " + str(Sy_l))
    print("\tS''(y) = " + str(Sy_ll), '\n')
    
    print("\tS(z) = " + str(Sz))
    print("\tS'(z) = " + str(Sz_l))
    print("\tS''(z) = " + str(Sz_ll), '\n')
    
    print("\tQC(y) = " + str(qc_y))
    print("\tError(y) = " + str(error_y), '\n')
    
    print("\tQC(z) = " + str(qc_z))
    print("\tError(z) = " + str(error_z), '\n')
    
    return  qc_y, qc_z, error_y, error_z
    

h = 0.05
x0 = 0
y0 = 1
z0 = 1
xi = 0


xf = 0.1
print("---------------Euler method--------------", '\n')
print("h = " + str(h), '\n')
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, z0, xi, xf, h, euler)
xf = 0.5
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, z0, xi, xf, h, euler)
print("------------------------------------------", '\n\n')


xf = 0.1
print("-----------------RK2 method---------------", '\n')
print("h = " + str(h), '\n')
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, z0, xi, xf, h, rk2)
xf = 0.5
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, z0, xi, xf, h, rk2)
print("------------------------------------------", '\n\n')
