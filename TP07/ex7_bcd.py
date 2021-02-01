def f_x(x, y, z):
    return (20 + y -2*z)/4


def f_y(x, y, z):
    return (25 - x - 2*z)/8


def f_z(x, y, z):
    return (-10 - 3*x + y)/5


def gaussJacobi(x0, y0, z0, k):
    xn = x0
    yn = y0
    zn = z0
    
    for i in range(0, k):
        xn = f_x(x0, y0, z0)
        yn = f_y(x0, y0, z0)
        zn = f_z(x0, y0, z0)
        
        x0 = xn 
        y0 = yn
        z0 = zn
        
    return xn, yn, zn


def gaussSeidel(x0, y0, z0, k):
    xn = x0
    yn = y0
    zn = y0
    
    for i in range(0, k):
        xn = f_x(x0, y0, z0)
        x0 = xn
        
        yn = f_y(x0, y0, z0)
        y0 = yn
        
        zn = f_z(x0, y0, z0)
        z0 = zn
        
    return xn, yn, zn


def relativeError(val1, val2):
    return abs(val1 - val2)/val2


x0 = 0
y0 = 0
z0 = 0
k = 5


# Khalesky method results
x_res = 9.35897435897436
y_res = 3.675213675213675
z_res = -6.880341880341881


print("---------------Gauss-Jacobi Method---------------",'\n')
print("k = " + str(k), '\n')
x, y, z = gaussJacobi(x0, y0, z0, k)
print("\tx = " + str(x))
print("\ty = " + str(y))
print("\tz = " + str(z), '\n')
print("\tError(x) = " + str(relativeError(x_res, x)))
print("\tError(y) = " + str(relativeError(y_res, y)))
print("\tError(z) = " + str(relativeError(z_res, z)), '\n')
print("-------------------------------------------------", '\n\n')


print("---------------Gauss-Seidel Method---------------",'\n')
print("k = " + str(k), '\n')
x, y, z = gaussSeidel(x0, y0, z0, k)
print("\tx = " + str(x))
print("\ty = " + str(y))
print("\tz = " + str(z), '\n')
print("\tError(x) = " + str(relativeError(x_res, x)))
print("\tError(y) = " + str(relativeError(y_res, y)))
print("\tError(z) = " + str(relativeError(z_res, z)), '\n')
print("-------------------------------------------------", '\n\n')
        



