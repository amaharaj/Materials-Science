# Question 3: At the bottom of the script there are calls to each function, uncomment to view the lattice. To change the number of unit cells change Number_of_Units as seen below. 

# Question 4: I am using get_distance() to call the pairwise interaction function. Uncomment the Simple Cubic, Body-Centered Cubic, or Face-Centered Cubic before uncommenting the get_distance() function to view the energy/convergence.  

import numpy as np
import math

back = open('BL14.xyz', 'w+')
back.readlines()

Number_of_Units = 1

# Specify Atom
atoms = "C"

# initialize coordinates
x = 0
y = 0
z = 0
coords = [[x,y,z]]

Category = 0

def User_Input(a,b,c,alpha,beta,gamma,Type):

    if a == b == c and alpha == beta == gamma == 90:
        if Type == "Simple":
            sc(a,b,c,alpha,beta,gamma,Type)
            Category = 1
            print "Generating Simple Cubic Structure"
        elif Type == "Body":
            bcc(a,b,c,alpha,beta,gamma,Type)
            Category = 1
            print "Generating Body-Centered Cubic Structure"
        elif Type == "Face":
            fcc(a,b,c,alpha,beta,gamma,Type)
            Category = 1
            print "Generating Face-Centered Cubic Structure"

    if a == b and b != c or a == c and c != b or b == c and c != a and alpha == beta == gamma == 90:
        if Type == "Simple":
            st(a,b,c,alpha,beta,gamma,Type)
            Category = 2
            print "Generating Simple Tetragonal Structure"
        elif Type == "Body":
            bct(a,b,c,alpha,beta,gamma,Type)
            Category = 2
            print "Generating Body-Centered Tetragonal Structure"

    if a != b and b!= c and alpha == beta == gamma == 90:
        if Type == "Simple":
            so(a,b,c,alpha,beta,gamma,Type)
            Category = 3
            print "Generating Simple Orthorhombic Structure"

        elif Type == "Body":
            bco(a,b,c,alpha,beta,gamma,Type)
            Category = 3
            print "Generating Body-Centered Orthorhombic Structure"

        elif Type == "End":
            eco(a,b,c,alpha,beta,gamma,Type)
            Category = 3
            print "Generating End-Centered Orthorhombic Structure"
        
        elif Type == "Face":
            fco(a,b,c,alpha,beta,gamma,Type)
            Category = 3 
            print "Generating Face-Centered Orthorhombic Structure"

    if a == b == c and alpha == beta == gamma < 120 and alpha != 90:
        if Type == "Rhomb":
            Rhomb(a,b,c,alpha,beta,gamma,Type)
            Category = 4
            print "Generating Rhombohedral Structure"

    if a == b != c and alpha == beta == 90 and gamma == 120:
        if Type == "Hexagonal":
            Hex(a,b,c,alpha,beta,gamma,Type)
            Category = 5
            print "Generating Hexagonal Structure"

    if a != b != c and alpha == gamma == 90 and alpha != beta:
        if Type == "Simple":
            scm(a,b,c,alpha,beta,gamma,Type)
            Category = 6
            print "Generating Simple Monoclinic Structure"
        elif Type == "End":
            ecm(a,b,c,alpha,beta,gamma,Type)
            Category = 6
            print "Generating Simple Monoclinic Structure"

    if a != b != c and alpha != beta != gamma:
        if Type == "Triclinic":
            Tri(a,b,c,alpha,beta,gamma,Type)
            Category = 7
            print "Generating Triclinic Structure"
 
    Number_of_Atoms(Type, Category)

def Number_of_Atoms(Type, Category):
  
    if Type == "Simple" and Category == 1:
                
        Number_of_Atoms = 8 + 4*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")    
        back.write("\n")

    if Type == "Body" and Category == 1:

        Number_of_Atoms = 9 + 5*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")
        back.write("\n")
    
    if Type == "Face" and Category == 1:

        Number_of_Atoms = 14 + 9*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")
        back.write("\n")

    if Type == "Simple" and Category == 2:
                        
        Number_of_Atoms = 8 + 4*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")
        back.write("\n")

    if Type == "Body" and Category == 2:

        Number_of_Atoms = 9 + 5*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")
        back.write("\n")
    
    if Type == "Simple" and Category == 3:
        Number_of_Atoms = 8 + 4*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")
        back.write("\n")    

    if Type == "Body" and Category == 3:
        Number_of_Atoms = 9 + 5*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")
        back.write("\n")

    if Type == "End" and Category == 3:
        Number_of_Atoms = 10 + 6*(Number_of_Units-1)
        back.write(str(Number_of_Atoms)+"\n")
        back.write("\n")

    if Type == "Face" and Category == 3:

        Number_of_Atoms = 14 + 9*(Number_of_Units-1)
        back.write(str(Number_of_Atoms) + "\n")
        back.write("\n")

    if Type == "Rhomb" and Category == 4:
       
        Number_of_Atoms = 8 + 4*(Number_of_Units-1)
        back.write(str(Number_of_Atoms)+ "\n")
        back.write("\n")

    if Type == "Hexagonal" and Category == 5:

        Number_of_Atoms = 14 + 12*(Number_of_Units-1)
        back.write(str(Number_of_Atoms)+ "\n")
        back.write("\n")

    if Type == "Simple" and Category == 6:

        Number_of_Atoms = 8 + 4*(Number_of_Units-1)
        back.write(str(Number_of_Atoms)+ "\n")
        back.write("\n")

    if Type == "End" and Category == 6:

        Number_of_Atoms = 10 + 6*(Number_of_Units-1)
        back.write(str(Number_of_Atoms)+ "\n")
        back.write("\n")

    if Type == "Triclinic" and Category == 7:

        Number_of_Atoms = 8 + 4*(Number_of_Units-1)
        back.write(str(Number_of_Atoms)+ "\n")
        back.write("\n")


def sc(a,b,c, alpha, beta, gamma, Type):

    # Create Unit Cell      
    coords.append([x,y+b,z])
    coords.append([x,y+b,z+c])
    coords.append([x,y,z+c])   
    
    # Generate Repeat Unit
    i = 0
    while i < Number_of_Units:
        coords.append([x+a+a*i,y,z])
        coords.append([x+a+a*i,y,z+c])
        coords.append([x+a+a*i,y+b,z])
        coords.append([x+a+a*i,y+b,z+c])
        i += 1
    
def bcc(a,b,c, alpha, beta, gamma, Copy):
    # create basic unit cell
    sc(a,b,c,alpha,beta,gamma,Copy)
    
    i = 0
    while i < Number_of_Units:
        coords.append([float(a)/2 +a*i, float(b)/2, float(c)/2])
        i += 1
    
def fcc(a,b,c, alpha, beta, gamma, Copy):

    sc(a,b,c,alpha,beta,gamma,Copy)

    coords.append([x,float(y+a)/2,float(z+a)/2])
    
    i = 0
    while i < Number_of_Units:
        coords.append([float(x+a)/2 + a*i,float(y+a)/2,z])
        coords.append([float(x+a)/2 + a*i,y,float(z+a)/2])
        coords.append([x+a+a*i,float(y+a)/2,float(z+a)/2])
        coords.append([float(x+a)/2 + a*i,y+a,float(z+a)/2])
        coords.append([float(x+a)/2 + a*i,float(y+a)/2,z+a])
        i += 1

def st(a,b,c, alpha, beta, gamma, Type):
     
    sc(a,b,c,alpha,beta,gamma,Type)   

def bct(a,b,c, alpha, beta, gamma, Type):
    # create basic unit cell
    sc(a,b,c,alpha,beta,gamma,Type)
    i = 0
    while i < Number_of_Units:
        coords.append([float(a)/2 + a*i, float(b)/2, float(c)/2])
        i += 1
def so(a,b,c, alpha, beta, gamma, Type):
    sc(a,b,c,alpha,beta,gamma,Type)

def bco(a,b,c, alpha, beta, gamma, Copy):
    sc(a,b,c,alpha,beta,gamma,Copy)
    i = 0
    while i < Number_of_Units:
        coords.append([float(a)/2 + a*i, float(b)/2, float(c)/2])
        i += 1

def eco(a,b,c, alpha, beta, gamma, Type):
    
    sc(a,b,c,alpha,beta,gamma,Type)

    i = 0
    while i < Number_of_Units:
        if a > b and a > c:
        
            coords.append([x+a*i, float(y+b)/2, float(z+c)/2])
            coords.append([x+a+a*i, float(y+b)/2, float(z+c)/2])
            i += 1

        elif b > a and b > c:

            coords.append([float(x+a)/2+a*i, y, float(z+c)/2])
            coords.append([float(x+a)/2+a*i, y+b, float(z+c)/2])
            i += 1 
  
        elif c > b and c > a:

            coords.append([float(x+a)/2+a*i, float(y+b)/2, z])
            coords.append([float(x+a)/2+a*i, float(y+b)/2, z+c])
            i += 1

def fco(a,b,c, alpha, beta, gamma, Type):

    sc(a,b,c,alpha,beta,gamma,Type)
    coords.append([x,float(y+b)/2,float(z+c)/2])

    i = 0
    while i < Number_of_Units:
        coords.append([float(x+a)/2 + a*i,float(y+b)/2,z])
        coords.append([float(x+a)/2 + a*i,y,float(z+c)/2])
        coords.append([x+a + a*i,float(y+b)/2,float(z+c)/2])
        coords.append([float(x+a)/2 + a*i,y+b,float(z+c)/2])
        coords.append([float(x+a)/2 + a*i,float(y+b)/2,z+c])
        i += 1

def Rhomb(a,b,c,alpha,beta,gamma,Type):

    xs = float(math.sin(alpha)*a)
    xl = float(math.cos(alpha)*a)

    ys = float(math.sin(beta)*b)
    yl = float(math.cos(beta)*b)
  
    zs = float(math.sin(gamma)*c)
    zl = float(math.cos(gamma)*c)

    coords.append([x+xs,y,z+zl])
    coords.append([x+xs,y+yl,z+zs])
    coords.append([x+2*xs,y+yl,z+zs+zl])

    i = 0
    while i < Number_of_Units:
        coords.append([x+a+a*i,y,z])
        coords.append([x+xs+a+a*i,y,z+zl])
        coords.append([x+a+xs+a*i,y+yl,z+zs])
        coords.append([x+a+2*xs+a*i,y+yl,z+zs+zl])
        i += 1 

def Hex(a,b,c,alpha,beta,gamma,Type):

    s = float(math.sin(math.pi/2 - math.pi*gamma/(2*180))*a)
    l = float(math.cos(math.pi/2 - math.pi*gamma/(2*180))*a)
    d = a + 2*s

    coords.append([x,y+c,z])

    i = 0
    while i < Number_of_Units:
        coords.append([x+s+d*i,y,z+l])
        coords.append([x+a+2*s+d*i,y,z])
        coords.append([x+s+d*i,y,z-l])
        coords.append([x+s+d*i,y+c,z+l])
        coords.append([x+a+2*s+d*i,y+c,z])
        coords.append([x+s+d*i,y+c,z-l])
        coords.append([x+a+s+d*i,y+c,z+l])
        coords.append([x+a+s+d*i,y+c,z-l])
        coords.append([x+a+s+d*i,y,z+l])
        coords.append([x+a+s+d*i,y,z-l])
        coords.append([x+float((a+2*s)/2)+d*i,y,z])
        coords.append([x+float((a+2*s)/2)+d*i,y+c,z])
        i += 1

def scm(a,b,c,alpha,beta,gamma,Type):

    s = float(math.cos(beta)*c)
    l = float(math.sin(beta)*c)

    coords.append([x,y,z+b])
    coords.append([x+s,y+l,z])
    coords.append([x+s,y+l,z+b])

    i = 0
    while i < Number_of_Units:
        coords.append([x+a+a*i,y,z])
        coords.append([x+a+a*i,y,z+b])
        coords.append([x+s+a+a*i,y+l,z])
        coords.append([x+s+a+a*i,y+l,z+b])
        i += 1
    

def ecm(a,b,c,alpha,beta,gamma,Type):

    s = float(math.cos(beta)*c)
    l = float(math.sin(beta)*c)

    scm(a,b,c,alpha,beta,gamma,Type)

    i = 0
    while i < Number_of_Units:    
        coords.append([x+float(a/2)+a*i,y, z+float(b/2)])
        coords.append([x+s+float(a/2)+a*i, y+l, z+float(b/2)])
        i += 1

def Tri(a,b,c,alpha,beta,gamma,Type):

    Rhomb(a,b,c,alpha,beta,gamma,Type)    

def get_distance(coords, Type):
 
    Atom_Array = []
    Atom = 0
    radius = []
    same_atom = True

    for c in coords:
        Atom += 1
        for o in coords:
            if c == o:
                same_atom = False
            else:
                x_dist = float(c[0]) - float(o[0])
                y_dist = float(c[1]) - float(o[1])
                z_dist = float(c[2]) - float(o[2])
                r = math.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
                radius.append(r)
            if c != o:
                Atom_Array.append(Atom)

    pairwise_potential(radius, Atom_Array,Atom, Type)

def pairwise_potential(radius,Atom_Array,Atom,Type):
    
    e = 10
    r_m = 2    

    V_convergence = []
    for d, a in zip(radius,Atom_Array):
        V = e*((r_m/d)**(12)-2*((r_m/d)**(6))) 
        V_convergence.append(float(V))   
        print "The energy for Atom ", a, "is: ", V

def Convergence(radius, Atom, Type,V_convergence):
 
    if Type == "Simple":
        Number_of_Atoms = 8 + 4*(Number_of_Units-1)

    elif Type == "Body":
        Number_of_Atoms = 9 + 5*(Number_of_Units-1)

    elif Type == "Face":
        Number_of_Atoms = 14 + 9*(Number_of_Units-1)    

    n = (Number_of_Atoms**2 - Atom)/Atom

    a = 1
    for i in xrange(0, len(V_convergence), n):
        y = V_convergence[i:i+n]
        while a <= Atom:
            print "Convergence for Atom ",a ," at: ", max(y)
            a += 1  

Simple_Cubic = User_Input(5,5,5,90,90,90,"Simple")
#Body_Centered_Cubic = User_Input(5,5,5,90,90,90,"Body")
#Face_Centered_Cubic = User_Input(5,5,5,90,90,90,"Face")
#Simple_Tetragonal = User_Input(5,5,10,90,90,90,"Simple")
#Body_Tetragonal = User_Input(5,5,10,90,90,90,"Body")
#Simple_Orthorhombic = User_Input(8,10,12,90,90,90,"Simple")
# Body_Centered_Orthorhombic = User_Input(8,10,12,90,90,90,"Body")
#End_Centered_Orthorhombic = User_Input(8,10,12,90,90,90,"End")
#Face_Centered_Orthorhombic = User_Input(8,10,12,90,90,90,"Face") 
#Rhombohedral = User_Input(5,5,5,60,60,60,"Rhomb")
#Hexagonal = User_Input(5,5,10,90,90,120,"Hexagonal")
#Simple_Monoclinic = User_Input(8,10,12,90,45,90,"Simple")
#End_Centered = User_Input(6,10,12,90,45,90,"End")
#Triclinic = User_Input(8,10,12,30,45,60,"Triclinic")

get_distance(coords,"Simple")


cartesian = []

for c in coords: 
 
        c.insert(0,atoms)
        cartesian.append(c)

for x in cartesian: 
        
        line = str(x[0]) + " "  + str(x[1]) + " " + str(x[2]) + " " + str(x[3]) + "\n" 
        back.write(line)
        
back.close()
