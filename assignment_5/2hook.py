import math


k = 20.0
m = 3.0
x_0 = 4.0
x_02 = 2.0
x = 2.0
x2 = 8.0
a = 0
a2 = 0
v = 0
v2 = 0
t = 0
KE = 0
PE = 0
E_Tot = 0

dt = 0.001
for i in range(10000):
    
    a = -k*(x-x_0) + k*(x2-x-x_0)/m
    a2 = -k*(x2-x-x_02)/m
    v = v + a*dt
    v2 = v2 + a2*dt
    x = x + v*dt
    x2 = x2 + v2*dt
    t = i*dt
    KE = (1.0/2.0)*m*(v**2)
    PE = (1.0/2.0)*k*(x-x_0)**2
    E_Tot = KE + PE

    print t, x, x2

