def f(x, y):
    return x**2 - 2*(y**2) + x*(y**3)

vertex_sum = f(0, -1) + f(0, 1) + f(2, -1) + f(2, 1)
center_sum = f(1, 0)
midpoint_sum = f(1, -1) + f(1, 1) + f(0, 0) + f(2, 0)

n_x = 2
n_y = 2

h_x = (2 - 0)/n_x
h_y = (1 - (-1))/n_y

trapezoidal = ((h_x*h_y)/4) * (vertex_sum + 2*midpoint_sum + 4*center_sum)
simpson = ((h_x*h_y)/9) * (vertex_sum + 4*midpoint_sum + 16*center_sum)

print("***************Trapezoidal rule***************", '\n')
print("Result = " + str(trapezoidal), '\n')
print("**********************************************", '\n')

print("****************Simpson's rule****************", '\n')
print("Result = " + str(simpson), '\n')
print("**********************************************", '\n')