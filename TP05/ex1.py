import math

def f(x):
    return math.sin(x)


def trapezoidal(x0, xn, n):
    h = (xn - x0)/n
    y0 = f(x0)
    yn = f(xn)
    counter = 0
    
    for i in range(1, n):
        counter += f(x0 + (h*i))
        
    return (h/2 * (y0 + yn + 2*counter))


def simpson(x0, xn, n):
    n *= 2
    h = (xn - x0)/n
    y0 = f(x0)
    yn = f(xn)
    counter_odd = 0
    counter_even = 0
    
    for i in range(1, n, 2):
        counter_odd += f(x0 + (h*i))
        
    for i in range(2, n - 1,2):
        counter_even += f(x0 + (h*i))
        
    return ((h/3) * (y0 + yn + 4*counter_odd + 2*counter_even))
         

def convergenceQuotient(x0, xn, n, rule):
    S = rule(x0, xn, n)
    S_l = rule(x0, xn, n*2)
    S_ll = rule(x0, xn, n*4)
    
    return (S_l - S)/(S_ll - S_l)


x0 = 0
xn = math.pi
n = [4, 8, 16, 64]


print("****************Trapezoidal rule*****************\n")
for i in n:
    print("n = " + str(i))
    print("\tResult: " + str(trapezoidal(x0,xn,i)))
print('')
for i in range(0, 2):
    print("\tQC(" + str(i+1) + ") = " + str(convergenceQuotient(x0, xn, n[i], trapezoidal)))
print("\n*************************************************\n\n")


print("*****************Simpson's rule******************\n")
for i in n:
    print("n = " + str(i))
    print("\tResult: " + str(simpson(x0,xn,i)))
print('')
for i in range(0, 2):
    print("\tQC(" + str(i+1) + ") = " + str(convergenceQuotient(x0, xn, n[i], simpson)))
print("\n*************************************************\n")

