def diff_x(x, y):
    return x*(y**2) - 1.1*x


def euler(x0, y0, yi, yf, h):
    n = round((yf - yi)/h)
    xn = x0
    yn = y0
    
    for i in range(0, n):
        xn = xn + h * diff_x(xn, yn)
        yn = yn + h
        
    return xn

def convergenceQuotientError(x0, y0, yi, tf, h):
    S = euler(x0, y0, yi, yf, h*4)
    S_l = euler(x0, y0, yi, yf, h*2)
    S_ll = euler(x0, y0, yi, yf, h)
    
    qc = (S_l - S)/(S_ll - S_l)
    error = S_ll - S_l
    
    print("\t\t\t\tS = " + str(S))
    print("\t\t\t\tS' = " + str(S_l))
    print("\t\t\t\tS'' = " + str(S_ll), '\n')
    
    print("\t\t\t\tQC = " + str(qc))
    print("\t\t\t\tError = " + str(error), '\n')
    
    return qc, error

n = 12
x0 = 1
y0 = 0
yi = 0
yf = 2.4 

print("-------------------------Euler method-------------------------", '\n')
h = round((yf - yi)/n, 1)
print("Integration step (h) = " + str(h) + " since there are " + str(n) + " intervals.",'\n')
convergenceQuotientError(x0, y0, yi, yf, h)
print("--------------------------------------------------------------")