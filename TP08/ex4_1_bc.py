points = {0.00 : 2,
          0.05 : 1.855,
          0.10 : 1.721, 
          0.15 : 1.6015, 
          0.20 : 1.482, 
          0.25 : 1.375, 
          0.30 : 1.275,
          0.35 : 1.1865, 
          0.40 : 1.098, 
          0.45 : 1.0215, 
          0.50 : 0.945, 
          0.55 : 0.876, 
          0.60 : 0.813}


def trapezoidal(xi, xf, h):
    n = round((xf - xi)/h)
    y0 = points[xi]
    yn = points[xf]
    area = 0
    
    for i in range(1, n):
        area += points[round(xi + i*h, 3)]
        
    return (h/2) * (y0 + yn + 2*area)


def simpson(xi, xf, h):
    n = round((xf - xi)/h)
    y0 = points[xi]
    yn = points[xf]
    area_odd = 0
    area_even = 0
    
    for i in range(1, n, 2):
        area_odd += 4 * points[round(xi + i*h, 3)]
    
    for i in range(2, n-1, 2):
        area_even += 2 * points[round(xi + i*h, 3)]
        
    return (h/3) * (y0 + yn + area_odd + area_even)
          

def relativeError(val1, val2):
    return abs(val1 - val2)/val1


xi = 0
xf = 0.6
h = 0.1
value = 0.7912404536792008


print("---------------Trapezoidal rule---------------", '\n')
print("h = " + str(h), '\n')
S = trapezoidal(xi, xf, h)
print("S = " + str(S))
print("Error = " + str(relativeError(value, S) * 100) + "%", '\n')
print("----------------------------------------------", '\n\n')


print("----------------Simpson's rule----------------", '\n')
print("h = " + str(h), '\n')
S = simpson(xi, xf, h)
print("S = " + str(S))
print("Error = " + str(relativeError(value, S) * 100) + "%", '\n')
print("----------------------------------------------", '\n\n')

