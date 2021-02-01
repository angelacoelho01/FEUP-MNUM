def f_x1(x1, x2, x3):
    return (27 - 2*x2 + x3)/10

def f_x2(x1, x2, x3):
    return (-61.5 + 3*x1 - 2*x3)/(-6)

def f_x3(x1, x2, x3):
    return (-21.5 - x1 - x2)/5

def gaussJacobi(x1_0, x2_0, x3_0, k):
    x1_n = x1_0
    x2_n = x2_0
    x3_n = x3_0
    
    for i in range(0, k):
        print("k = " + str(i))
        print("\tx1 = " + str(x1_n))
        print("\tx2 = " + str(x2_n))
        print("\tx3 = " + str(x3_n), '\n')
        
        x1_n = f_x1(x1_0, x2_0, x3_0)
        x2_n = f_x2(x1_0, x2_0, x3_0)
        x3_n = f_x3(x1_0, x2_0, x3_0)
        
        x1_0 = x1_n
        x2_0 = x2_n
        x3_0 = x3_n
        
    return x1_n, x2_n, x3_n

def gaussSeidel(x1_0, x2_0, x3_0, k):
    x1_n = x1_0
    x2_n = x2_0
    x3_n = x3_0
    
    for i in range(0, k):
        print("k = " + str(i))
        print("\tx1 = " + str(x1_n))
        print("\tx2 = " + str(x2_n))
        print("\tx3 = " + str(x3_n), '\n')
        
        x1_n = f_x1(x1_0, x2_0, x3_0)
        x1_0 = x1_n
        
        x2_n = f_x2(x1_0, x2_0, x3_0)
        x2_0 = x2_n
        
        x3_n = f_x3(x1_0, x2_0, x3_0)
        x3_0 = x3_n

    return x1_n, x2_n, x3_n
    
guess_x1 = 0
guess_x2 = 0
guess_x3 = 0
k = 4


print("---------------Gauss-Jacobi method---------------", '\n')
gaussJacobi(guess_x1, guess_x2, guess_x3, k)
print("-------------------------------------------------", '\n\n')


print("---------------Gauss-Seidel method---------------", '\n')
gaussSeidel(guess_x1, guess_x2, guess_x3, k)
print("-------------------------------------------------", '\n\n')



