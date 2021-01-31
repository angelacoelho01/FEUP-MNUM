import math

def f(x):
    return 1 - math.exp(-2*x)


def trapezoidal(x0, xn, n):
    y0 = f(x0)
    yn = f(xn)
    h = (xn - x0)/n
    counter = 0
    
    for i in range(1, n):
        counter += f(x0 + (i*h))
        
    return (h/2) * (y0 + yn + 2*counter)


def simpson(x0, xn, n):
    y0 = f(x0)
    yn = f(xn)
    h = (xn - x0)/n
    counter_odd = 0
    counter_even = 0
    
    for i in range(1, n, 2):
        counter_odd += f(x0 + (h*i))
        
    for i in range(2, n-1, 2):
        counter_even += f(x0 + (h*i))
        
    return (h/3) * (y0 + yn + 4*counter_odd + 2*counter_even)
    


def convergenceQuotient(x0, xn, n, rule):
    S = rule(x0, xn, n)
    S_l = rule(x0, xn, 2*n)
    S_ll = rule(x0, xn, 4*n)
    
    return (S_l - S)/(S_ll - S_l)

x0 = 0
xn = 4
n = [4, 8, 16, 32, 64]


print("****************Trapezoidal rule****************\n")
for i in n:
    print("n = " + str(i))
    print("\tResult: " + str(trapezoidal(x0,xn,i)))
    print("\tConvergence quocient: " + str(convergenceQuotient(x0, xn, i, trapezoidal)), '\n')
print("*************************************************\n\n")


print("******************Simpson rule*******************\n")
for i in n:
    print("n = " + str(i))
    print("\tResult: " + str(simpson(x0,xn,i)))
    print("\tConvergence quocient: " + str(convergenceQuotient(x0, xn, i, simpson)), '\n')
print("*************************************************\n")




    