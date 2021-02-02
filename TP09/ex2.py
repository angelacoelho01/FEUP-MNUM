import math

tolerance=  0.001

def f(x, y):
    return math.sin(x/2) + x**2 - math.cos(y)


def product_x(x, y):
    return -(8*x + 2*math.cos(x/2))/(math.sin(x/2) - 8)


def product_y(x, y):
    return math.sin(y)/math.cos(y)


def absoluteError(error_x, error_y):
    return (error_x <= tolerance) and (error_y <= tolerance)


def quadratic(x0, y0):
    xn = x0
    yn = y0
    stopCondition = False
    no_iter = 0
    
    while not stopCondition:
        x_temp = xn - product_x(xn, yn)
        y_temp = yn - product_y(xn, yn)
        
        error_x = abs(x_temp - xn)
        error_y = abs(y_temp - yn)
        stopCondition = absoluteError(error_x, error_y)
            
        xn = x_temp
        yn = y_temp
        no_iter += 1
        
    return xn, yn, no_iter, error_x, error_y


x0 = -3
y0 = -1


print("---------------Quadratic method---------------")
x, y, no_iter, error_x, error_y = quadratic(x0, y0)
print("No iterations = " + str(no_iter), '\n')
print("x = " + str(x))
print("y = " + str(y), '\n')
print("f(x, y) = " + str(f(x, y)), '\n')
print("Error(x) = " + str(error_x))
print("Error(y) = " + str(error_y), '\n')
print("----------------------------------------------")
    
    