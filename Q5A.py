import math

mass_H = 1.0079

m1 = mass_H
m2 = mass_H

kb = 1.3806*10**(-23)
DOF = 6
T = 5000
vel = math.sqrt((2*DOF*kb*T)/(mass_H))
E_g = 4.52
h = 4.13567*10**(-15)
F_vib = 1.1*10**3

k = F_vib

r1 = 0.0
r2 = 2.5

r_0 = 2.0
dist = 0

a1 = 0
a2 = 0

v1 = vel
v2 = vel

t = 0.0
e = 10

dt = 0.001
for i in range(10000):

    d = math.sqrt((r2-r1)**2)

    dist += d

    a1 = (k*(d - r_0) + e*(-12*(r_0/d)**13 + 2*6*(r_0/d)**7))/m1    
    a2 = (-k*(d-r_0) - e*(-12*(r_0/d)**13 + 2*6*(r_0/d)**7))/m2

    v1 = v1 + a1*dt
    v2 = v2 + a2*dt

    r1 = r1 + v1*dt
    r2 = r2 + v2*dt

    t = i*dt + dt

    print t, r1, r2, dist/(i+1)

