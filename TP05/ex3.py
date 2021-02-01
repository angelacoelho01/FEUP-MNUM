values = {-2 : 35,
          0 : 5,
          2 : -10,
          4 : 2,
          6 : 5,
          8 : 3,
          10 : 20}

def trapezoidal(x0, xn, n):
    h = (xn - x0)/n
    y0 = values[x0]
    yn = values[xn]
    area = 0
    
    for i in range(1, n):
        area += values[x0 + i*h]
        
    return (h/2) * (y0 + yn + 2*area)

def simpson(x0, xn, n):
    n *= 2
    h = (xn - x0)/n
    y0 = values[x0]
    yn = values[xn]
    area = 0
    
    for i in range(1, n):
        if i%2 == 0:
            area += 2*values[x0 + i*h]
        else:
            area += 4*values[x0 + i*h]
            
    return (h/3) * (y0 + yn + area)
    
x0 = -2
xn = 10
n = 6 # h = 2
print("**********Trapezoidal rule**********\n")
print("n = " + str(n))
print("S = " + str(trapezoidal(x0, xn, n)), '\n')
print("************************************\n\n")
n = 3 # h = 2 since in simpson's rule 2*n
print("***********Simpson's rule***********\n")
print("n = " + str(n))
print("S = " + str(simpson(x0, xn, n)), '\n')
print("************************************")



