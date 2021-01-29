guess_a = 4.52
guess_b = 4.54
error = 10**(-5)

def f(x):
    return -1 + 5.5*x - 4*(x**2) + 0.5*(x**3)


def diff_f(x):
    return 1.5*(x**2) - 8*x + 5.5


def stopCriterion(a, b):
    return abs(f(a) - f(b)) <= error


def newton(x):
    x_next = x
    stopCondition = False
    no_iter = 0
    
    while not stopCondition:
        # Test convergence
        if diff_f(x) == 0:
            print("Divergent.\n")
            return 
    
        x = x_next
        x_next = x - f(x)/diff_f(x)
        
        no_iter += 1
        stopCondition = stopCriterion(x, x_next)
        
    print("Number of iterations: " + str(no_iter))
    return x_next


print("Guess: " + str(guess_a))
print("Root: " + str(newton(guess_a)) + "\n")


print("Guess: " + str(guess_b))
print("Root: " + str(newton(guess_b)) + "\n")