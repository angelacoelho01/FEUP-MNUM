import time

"""Disclaimer: the results obtained do not match the solutions. """


error = 10**(-3)
a = -2
b = -1
time_max = 10


def f(x):
    return 5.5*(x**2) + 6.2*x - 2.1

def absoluteStopCriterion(a, b):
    return abs(a - b) <= error


def relativeStopCriterion(a, b):
    return abs((a - b)/a) <= error


def cancelFunctionCriterion(a, b):
    return abs(f(b) - f(a)) <= error


def relativeCancelFunctionCriterion(a, b):
    return abs((f(b) - f(a))/f(b)) <= error
    

# Only interval methods: bisection and false position
def bisection(a, b, stopCriterion):
    no_iter = 0
    start = time.time()
    
    while not stopCriterion(a, b):
        if (time.time() - start) > time_max:
            print("Took to long.\n")
            return 
            
        m = (a + b)/2
        
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
            
        no_iter += 1
    
    print("\nNumber of iterations: " + str(no_iter))
    return m


def falsePosition(a, b, stopCriterion):
    no_iter = 0
    start = time.time()
    
    while not stopCriterion(a, b):
        if (time.time() - start) > time_max:
            print("Took to long.\n")
            return
        
        m = (f(b)*a - f(a)*b)/(f(b) - f(a))
        
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
            
        no_iter += 1
        
    print("\nNumber of iterations: " + str(no_iter))
    return m


print("***************Bisection Method****************")
print("Interval: [" + str(a) + ", " + str(b) + "]\n")
print("Absolute stop criterion: " + str(bisection(a, b, absoluteStopCriterion)) + str("\n"))
print("Relative stop criterion: " + str(bisection(a, b, relativeStopCriterion)) + str("\n"))
print("Cancel function criterion: " + str(bisection(a, b, cancelFunctionCriterion)) + str("\n")) 
print("Relative cancel function criterion: " + str(bisection(a, b, relativeCancelFunctionCriterion)))
print("***********************************************\n\n")


print("*************False Position Method*************")
print("Interval: [" + str(a) + ", " + str(b) + "]\n")
print("Absolute stop criterion: " + str(falsePosition(a, b, absoluteStopCriterion)) + str("\n"))
print("Relative stop criterion: " + str(falsePosition(a, b, relativeStopCriterion)) + str("\n"))
print("Cancel function criterion: " + str(falsePosition(a, b, cancelFunctionCriterion)) + str("\n"))
print("Relative cancel function criterion: " + str(falsePosition(a, b, relativeCancelFunctionCriterion)))
print("***********************************************\n")


