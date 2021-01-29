import numpy as np 

# Value to use in stop criterion
error = 10**(-4)


def f(x):
    return x-2*np.log(x)-5


def diff_f(x):
    return 1 - 2/x


def picardPeano_f(x):
    return 2*np.log(x) + 5


def diff_picardPeano_f(x):
    return 2/(x**2)


def relativeStopCriterion(a, b):
    return abs(((a-b)/a)) <= error


# Interval methods: bisection and false position
def bisection(a, b):
    no_iter = 0
    
    while(not relativeStopCriterion(a, b)):
        m = (a + b)/2
        
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
            
        no_iter += 1
        
    print("\nNumber of iterations: " + str(no_iter))
    return m


def falsePosition(a, b):
    no_iter = 0
    
    while(not relativeStopCriterion(a, b)):
        m = (a*f(b) - b*f(a))/(f(b) - f(a))
        
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
            
        no_iter += 1
        
    print("\nNumber of iterations: " + str(no_iter))
    return m


# Non-interval methods: newton and Picard Peano
def newton(x):
    no_iter = 0
    stopCondition = False
    x_next = x
    
    while(not stopCondition):
        # Test convergence
        if diff_f(x) == 0:
            print("\nDivergent, try another guess.")
            return
        
        x = x_next
        x_next = x - f(x)/diff_f(x)
        
        stopCondition = relativeStopCriterion(x, x_next)
        no_iter += 1
    
    print("\nNumber of iterations: " + str(no_iter))
    return x_next


def picardPeano(x):
    no_iter = 0
    stopCondition = False
    x_next = x
    
    # Test convergence
    if not (abs(diff_picardPeano_f(x) < 1)):
        print("\nDivergent, try another guess.")
        return
    
    while(not stopCondition):
        
        
        x = x_next
        x_next = picardPeano_f(x)
        
        stopCondition = relativeStopCriterion(x, x_next)
        no_iter += 1
        
    print("\nNumber of iterations: " + str(no_iter))
    return x_next
    

print("*********Bisection Method*********")
a = input("Lower extreme: ")
b = input("Higher extreme: ")
print("\nRoot value: " + str(bisection(float(a), float(b))))
print("**********************************\n\n")


print("******False Position Method******")
a = input("Lower extreme: ")
b = input("Higher extreme: ")
print("\nRoot value: " + str(falsePosition(float(a), float(b))))
print("*********************************\n\n")


print("**********Newton Method**********")
guess = input("Guess: ")
print("\nRoot value: " + str(newton(float(guess))))
print("*********************************\n\n")


print("*******Picard Peano Method*******")
guess = input("Guess: ")
print("\nRoot value: " + str(picardPeano(float(guess))))
print("*********************************\n")
