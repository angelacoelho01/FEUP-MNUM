import math

k = 0

def diff_y(x, y, z):
    return -k*y + 4*math.exp(-x)


def diff_z(x, y, z):
    return -(y * (z**2))/3


def rk4(x0, y0, z0, n, h, _print):
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
        
        if _print == True:
            print("\tx = " + str(xn))
            print("\ty = " + str(yn))
            print("\tz = " + str(zn), '\n')
        
    return yn, zn


def convergenceQuotientError(x0, y0, z0, n, h):
    Sy, Sz = rk4(x0, y0, z0, n, h, False)
    Sy_l, Sz_l = rk4(x0, y0, z0, n, h/2, False)
    Sy_ll, Sz_ll = rk4(x0, y0, z0, n, h/4, False)
    
    qc_y = (Sy_l - Sy)/(Sy_ll - Sy_l)
    qc_z = (Sz_l - Sz)/(Sz_ll - Sz_l)
        
    error_y = (Sy_ll - Sy_l)/15
    error_z = (Sz_ll - Sz_l)/15
    
    print("\tQC(y) = " + str(qc_y))
    print("\tError(y) = " + str(error_y), '\n')
    
    print("\tQC(z) = " + str(qc_z))
    print("\tError(z) = " + str(error_z), '\n')
    
    return  qc_y, qc_z, error_y, error_z


x0 = 0
y0 = 2
z0 = 4
h = 0.1
n = 1


k = 0
print("----------------------RK4 method--------------------", '\n')
print("h = " + str(h), '\n')
print("k = " + str(k), '\n')
rk4(x0, y0, z0, n, h, True)
convergenceQuotientError(x0, y0, z0, n, h)
k = 2
print("k = " + str(k), '\n')
rk4(x0, y0, z0, n, h, True)
convergenceQuotientError(x0, y0, z0, n, h)
k = 6
print("k = " + str(k), '\n')
rk4(x0, y0, z0, n, h, True)
convergenceQuotientError(x0, y0, z0, n, h)
print("We can see that the table values are equal for k =2.",'\n')
k = 2
h = 0.2
print("k = " + str(k), '\n')
print("h = " + str(h), '\n')
rk4(x0, y0, z0, n, h, True)
convergenceQuotientError(x0, y0, z0, n, h)
h = 0.1
print("h = " + str(h), '\n')
rk4(x0, y0, z0, n, h, True)
convergenceQuotientError(x0, y0, z0, n, h)
h = 0.05
print("h = " + str(h), '\n')
rk4(x0, y0, z0, n, h, True)
convergenceQuotientError(x0, y0, z0, n, h)
print("----------------------------------------------------", '\n\n')

        
    
    