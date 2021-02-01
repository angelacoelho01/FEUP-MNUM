def diff_a(t, v, a):
    return 0.5*a - v


def diff_v(t, v, a):
    return a


def rk2(t0, v0, a0, ti, tf, h):
    n = round((tf - ti)/h)
    tn = t0
    vn = t0
    an = a0
    
    for i in range(0, n):
        delta_v = h * diff_v(t0 + h/2, v0 + (h/2 * diff_v(t0, v0, a0)), a0 + (h/2 * diff_a(t0, v0, a0)))
        delta_a = h * diff_a(t0 + h/2, v0 + (h/2 *diff_v(t0, v0, a0)), a0 + (h/2 * diff_a(t0, v0, a0)))
        
        tn = t0 + h
        vn = v0 + delta_v
        an = a0 + delta_a
        
        t0 = tn
        v0 = vn
        a0 = an
        
    return vn, an


def convergenceQuotientError(t0, v0, a0, ti, tf, h):
    Sy, Sz = rk2(t0, v0, a0, ti, tf, h)
    Sy_l, Sz_l = rk2(t0, v0, a0, ti, tf, h/2)
    Sy_ll, Sz_ll = rk2(t0, v0, a0, ti, tf, h/4)
    
    qc_y = (Sy_l - Sy)/(Sy_ll - Sy_l)
    qc_z = (Sz_l - Sz)/(Sz_ll - Sz_l)
    
    error_y = (Sy_ll - Sy_l)/3
    error_z = (Sz_ll - Sz_l)/3
    
    print("\tS(y) = " + str(Sy))
    print("\tS'(y) = " + str(Sy_l))
    print("\tS''(y) = " + str(Sy_ll), '\n')
    
    print("\tQC(y) = " + str(qc_y))
    print("\tError(y) = " + str(error_y), '\n')
    
    print("\tS(z) = " + str(Sz))
    print("\tS'(z) = " + str(Sz_l))
    print("\tS''(z) = " + str(Sz_ll), '\n')
    
    print("\tQC(z) = " + str(qc_z))
    print("\tError(z) = " + str(error_z), '\n')
    
    return qc_y, error_y, qc_z, error_z


ti = 0
tf = 4
t0 = 0
v0 = 2
a0 = 0
h = 0.01

print("---------------RK2 method---------------")
print("h = " + str(h), '\n')
print("t = " + str(tf), '\n')
convergenceQuotientError(t0, v0, a0, ti, tf, h)
print("----------------------------------------")

    
    
    
