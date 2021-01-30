import numpy as np


error = 10**(-3)
guess_x = 4
guess_y = 4
no_iter = 2


"""Note that in the pdf f1(x) is wrong, this is the right one."""
def f1(x, y):
    return 2*(x**2) - x*y - 5*x + 1


def diff_f1_x(x, y):
    return 4*x -y -5


def diff_f1_y(x, y):
    return -x


def f2(x, y):
    return x + 3 *np.log(x) - y**2


def diff_f2_x(x, y):
    return 1 + 3/x


def diff_f2_y(x, y):
    return -2*y


def newton(x, y, no_iter):
    x_next = x
    y_next = y
    counter_iter = 0 
    
    while counter_iter < no_iter:
        # Test convergence: determinant of J(xn, yn) must be different from 0
        aux = diff_f1_x(x, y)*diff_f2_y(x, y) - diff_f1_y(x, y)*diff_f2_x(x, y)
        if aux == 0:
            print("Divergent.\n")
            return
        
        x = x_next
        y = y_next
        
        print("Number of iteration: " + str(counter_iter))
        print("\tx = " + str(x))
        print("\ty = " + str(y))
        print("\tf1(x, y) = " + str(f1(x,y)))
        print("\tf2(x, y) = " + str(f2(x, y)))
        print("\tdiff_f1_x(x, y) = " + str(diff_f1_x(x, y)))
        print("\tdiff_f1_y(x, y) = " + str(diff_f1_y(x, y)))
        print("\tdiff_f2_x(x, y) = " + str(diff_f2_x(x, y)))
        print("\tdiff_f2_y(x, y) = " + str(diff_f2_y(x, y)) + "\n")
        
        
        x_next = x - (f1(x, y)*diff_f2_y(x, y) - f2(x, y)*diff_f1_y(x, y))/(diff_f1_x(x, y)*diff_f2_y(x, y) - diff_f2_x(x, y)*diff_f1_y(x, y))
        y_next = y - (f2(x, y)*diff_f1_x(x, y) - f1(x, y)*diff_f2_x(x, y))/(diff_f1_x(x, y)*diff_f2_y(x, y) - diff_f2_x(x, y)*diff_f1_y(x, y))

        counter_iter += 1
        
    return x_next, y_next


print("***************Newton Method***************\n")
x, y = newton(guess_x, guess_y, no_iter)
print("Result:")
print("\tx = " + str(x))
print("\ty = " + str(y))
print("\n*******************************************\n")

