import math


def diff_y(x, y, z):
    return z 


def diff_z(x, y, z):
    return -8*y -0.6*z


def rk4(x0, y0, z0, xi, xf, h):
    n = round((xf - xi)/h)
    xn = x0
    yn = x0
    zn = z0
    
    for i in range(0, n):
        delta_y1 = h * diff_y(x0, y0, z0)
        delta_z1 = h * diff_z(x0, y0, z0)
        
        delta_y2 = h * diff_y(x0 + (h/2), y0 + (delta_y1/2), z0 + (delta_z1/2))
        delta_z2 = h * diff_z(x0 + (h/2), y0 + (delta_y1/2), z0 + (delta_z1/2))
        
        delta_y3 = h * diff_y(x0 + (h/2), y0 + (delta_y2/2), z0 + (delta_z2/2))
        delta_z3 = h * diff_z(x0 + (h/2), y0 + (delta_y2/2), z0 + (delta_z2/2))
        
        delta_y4 = h * diff_y(x0 + h, y0 + delta_y3, z0 + delta_z3)
        delta_z4 = h * diff_z(x0 + h, y0 + delta_y3, z0 + delta_z3)        
        
        delta_y = (delta_y1/6) + (delta_y2/3) + (delta_y3/3) + (delta_y4/6)
        delta_z = (delta_z1/6) + (delta_z2/3) + (delta_z3/3) + (delta_z4/6)
        
        xn = x0 + h
        yn = y0 + delta_y
        zn = z0 + delta_z
        
        x0 = xn
        y0 = yn
        z0 = zn
        
    return yn, zn


def convergenceQuotientError(x0, y0, z0, xi, xf, h):
    Sy, Sz = rk4(x0, y0, z0, xi, xf, h)
    Sy_l, Sz_l = rk4(x0, y0, z0, xi, xf, h/2)
    Sy_ll, Sz_ll = rk4(x0, y0, z0, xi, xf, h/4)
    
    qc_y = (Sy_l - Sy)/(Sy_ll - Sy_l)
    qc_z = (Sz_l - Sz)/(Sz_ll - Sz_l)
        
    error_y = (Sy_ll - Sy_l)/15
    error_z = (Sz_ll - Sz_l)/15
    
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


x0 = 0
y0 = 4
z0 = 0
h = 0.1
xi = 0

print("-----------------RK4 method---------------", '\n')
xf = 0.1
print("h = " + str(h), '\n')
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, z0, xi, xf, h)
xf = 0.5
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, z0, xi, xf, h)
print("------------------------------------------", '\n\n')

        
    
    