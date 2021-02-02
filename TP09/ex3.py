import math

B = (math.sqrt(5) - 1)/2
A = B**2
tolerance = 0.001


def f(x):
    return (2*x + 1)**2 - (5*math.cos(10*x))

def absoluteError(val1, val2):
    return abs(val1 - val2) <= tolerance


def aurea(x1, x2, minimum):
    x3 = 0
    x4 = 0
    stopCondition = False
    
    while not stopCondition:    
        x3 = A * (x2 - x1) + x1
        x4 = B * (x2 - x1) + x1
        if minimum:
            condition = f(x3) < f(x4)
        else:
            condition = f(x3) > f(x4)
    
        if condition:
            x2 = x4
        else:
            x1 = x3
            
        stopCondition = absoluteError(x1, x2)
    
    return x1


x1 = -1
x2 = 0


print("---------------Aurea rule---------------", '\n')
minimum = aurea(x1, x2, True)
print("Minimum = " + str(minimum))
print("f(minimum) = " + str(f(minimum)),'\n')
maximum = aurea(x1, x2, False)
print("Maximum = " + str(maximum))
print("f(maximum) = " + str(f(maximum)), '\n')
print("-----------------------------------------")
            
