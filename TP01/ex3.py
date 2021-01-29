import math

# Just non-interval methods: newton and picard peano

guess = 4
no_iter = 3


def f(x):
    return x**2 - x - 1.2

def diff_f(x):
    return 2*x -1


def picardPeano_f(x):
    return math.sqrt(x + 1.2)


def diff_picardPeano_f(x):
    return 1/(2*math.sqrt(x + 1.2))


def newton(x, no_iter):
    x_next = x
    counter_iter = 0
    
    while counter_iter < no_iter:
        # Test convergence
        if diff_f(x) == 0:
            print("Divergent.\n")
            return
        
        print("Number of iterations: " + str(counter_iter))
        print("g(x) = " + str(picardPeano_f(x)))
        print("Root: " + str(x_next) + str("\n"))
            
        x = x_next
        x_next = x - f(x)/diff_f(x)
        
        counter_iter += 1
        
    return x_next


def picardPeano(x, no_iter):
    x_next = x
    counter_iter = 0
    
    # Test convergence
    if not abs(diff_picardPeano_f(x)) < 1:
        print("Divergent.\n")
        return
    
    while counter_iter < no_iter:
        print("Number of iterations: " + str(counter_iter))
        print("g(x) = " + str(picardPeano_f(x)))
        print("Root: " + str(x_next) + str("\n"))

        x = x_next
        x_next = picardPeano_f(x)
        
        counter_iter += 1
        
    return x_next


print("***************Newton Method***************\n")
print("Guess: " + str(guess) + "\n")
newton(guess, no_iter)
print("\n*******************************************\n\n")


print("************Picard Peano Method************\n")
print("Guess: " + str(guess) + "\n")
picardPeano(guess, no_iter)
print("\n*******************************************\n\n")

