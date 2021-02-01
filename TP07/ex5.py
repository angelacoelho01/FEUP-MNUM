def diff_z(x, y, z):
    return 0.5*z - y


def diff_y(x, y, z):
    return z


def rk2(x0, y0, z0, xi, xf, h):
    n = round((xf - xi)/h)
    xn = x0
    yn = y0
    zn = z0
    
    for i in range(0, n):
        delta_y = h * diff_y(x0 + h/2, y0 + h/2 * diff_y(x0, y0, z0), z0 + h/2 * diff_z(x0, y0, z0))
        delta_z = h * diff_z(x0 + h/2, y0 + h/2 * diff_y(x0, y0, z0), z0 + h/2 * diff_z(x0, y0, z0))
        
        xn = x0 + h
        yn = y0 + delta_y
        zn = z0 + delta_z
        
        x0 = xn
        y0 = yn
        z0 = zn
        
    return yn, zn


def convergenceQuotientError(x0, y0, z0, xi, xf, h):
    Sy, Sz = rk2(x0, y0, z0, xi, xf, h)
    Sy_l, Sz_l = rk2(x0, y0, z0, xi, xf, h/2)
    Sy_ll, Sz_ll = rk2(x0, y0, z0, xi, xf, h/4)
    
    qc_y = (Sy_l - Sy)/(Sy_ll - Sy_l)
    qc_z = (Sz_l - Sz)/(Sz_ll - Sz_l)
    
    error_y = (Sy_ll - Sy_l)/3
    error_z = (Sz_ll - Sz_l)/3
    
    print("\tS(y) = " + str(Sy))
    print("\tS'(y) = " + str(Sy_l))
    print("\tS''(y) = " + str(Sy_ll), '\n')
    
    print("\tQC(y) = " + str(qc_y))
    print("\tError(y) = " + str(error_y), '\n')
    
    print("\tS(z) = " + str(Sz))
    print("\tS'(z) = " + str(Sz_l))
    print("\tS''(z) = " + str(Sz_ll), '\n')
    
    print("\tQC(z) = " + str(qc_z))
    print("\tError(z) = " + str(error_z), "\n")
    

x0 = 2
y0 = 2
z0 = 0
xi = 0
xf = 4
h = 0.01

print("---------------RK2 method---------------", '\n')
print("h = " + str(h), '\n')
print("x = " + str(xf), '\n')
convergenceQuotientError(x0, y0, z0, xi, xf, h)
print("----------------------------------------", '\n')
    