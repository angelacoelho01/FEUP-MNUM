tolerance = 0.001

def f(x, y):
    return 2*x*y + 2*x - x**2 - 2*(y**2)


def diff_f_x(x, y):
    return 2*y - 2*x + 2


def diff_f_y(x, y):
    return 2*x - 4*y


def absoluteError(error_x, error_y):
    return (error_x <= tolerance) and (error_y <= tolerance)


def gradient(x0, y0, h):
    xn = x0
    yn = y0
    stopCondition = False
    no_iter = 0
    
    while not stopCondition:
        x_temp = xn + h * diff_f_x(xn, yn)
        y_temp = yn + h * diff_f_y(xn, yn)
        
        if f(x_temp, y_temp) > f(xn, yn):
            h *= 2
        else:
            h /= 2
            
        error_x = abs(xn - x_temp)
        error_y = abs(yn - y_temp)
        stopCondition = absoluteError(error_x, error_y)
            
        xn = x_temp
        yn = y_temp
        no_iter += 1
        
    return xn, yn, h, no_iter, error_x, error_y

x0 = -1
y0 = 1
h = 1

print("---------------Gradient method---------------", '\n')
x, y, h, no_iter, error_x, error_y = gradient(x0, y0, h)
print("h final = " + str(h), '\n')
print("No iterations = " + str(no_iter), '\n')
print("x = " + str(x))
print("y = " + str(y), '\n')
print("df/dx(x, y) = " + str(diff_f_x(x, y)))
print("df/dy(x, y) = " + str(diff_f_y(x, y)), '\n')
print("f(x, y) = " + str(f(x, y)), '\n')
print("Error(x) = " + str(error_x))
print("Error(y) = " + str(error_y), '\n')
print("----------------------------------------------")






    
    
    
    