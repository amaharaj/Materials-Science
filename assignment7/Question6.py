import os, sys
import numpy as np

back = open('xcoords.xyz', 'w+')
back.readlines()

mdx = open('MDX', 'w+' )
mdx.readlines()
mdy = open('MDY', 'w+')
mdy.readlines()

def dist(a,b):
    """
    Returns the distance between two vectors, a and b
    Will work for 2d and 3d vectors
    """
    dist = 0.

    for i in range(len(a)):
        dist += (b[i]-a[i])**2.
        dist = dist**.5
        return dist

def f_harm(a,b,c):
    r0 = 2.
    k = 1.1*10**3
    if c == "x":
        r = dist(a,b)
        mdx.write(str(r) + '\n')
        forceX = -k*(r - r0)
        return forceX
    if c == "y":
        r = dist(a,b)
        mdy.write(str(r) + '\n')
        forceY = -k*(r - r0)
        return forceY

def update_forces(atoms_list,c):
    forces = np.zeros((len(atoms_list),3),dtype=float) # create empty forces list
    natoms = len(atoms_list)
# Use neighbours on either side to set force. Ends will be wrong (see fix below)
# note that this assumes the spring is the x direction. No projections are being done!

    for i in range(natoms):
        forces[i][0] = -f_harm(atoms_list[i], atoms_list[(i+1)%natoms],"x") # atom to the right
        forces[i][0] += +f_harm(atoms_list[i-1],atoms_list[i],"x") # atom to the left
        

        forces[i][1] = -f_harm(atoms_list[i], atoms_list[(i+1)%natoms],"y")
        forces[i][1] += +f_harm(atoms_list[i-1],atoms_list[i],"y")
# Deal with the special case of the atoms at either end of the chain
    forces[0][0] = -f_harm(atoms_list[0], atoms_list[1], "x")
    # Right end must be fixed, so make sure no forces are being applied
    forces[-1][0] = +f_harm(atoms_list[-2], atoms_list[-1], "x")
    
    forces[0][1] = -f_harm(atoms_list[0], atoms_list[1], "y")
    # Atoms at the right end must be fixed. Make sure no force is applied. 
    forces[-1][1] = +f_harm(atoms_list[-2], atoms_list[-1], "y")
    return forces

def update_acc(atom_acc, atom_for, mass):
    natoms = len(atom_acc)
    for i in range(natoms):
        atom_acc[i][0] = atom_for[i][0]/mass
        atom_acc[i][1] = atom_for[i][1]/mass
    return atom_acc

def update_vel(atom_vel, atom_acc, dt):
    natoms = len(atom_vel)
    for i in range(natoms):
        atom_vel[i][0] += atom_acc[i][0]*dt
        atom_vel[i][1] += atom_acc[i][1]*dt
    return atom_vel

def update_pos(atom_pos, atom_vel, dt):
    natoms = len(atom_pos)
    for i in range(natoms):
        atom_pos[i][0] += atom_vel[i][0]*dt
        atom_pos[i][1] += atom_vel[i][1]*dt
    return atom_pos

def create_arrays(natoms):
    atom_pos = np.zeros((natoms,3), dtype=float) # empty list of atoms
    atom_vel = np.zeros((natoms,3), dtype=float)
    atom_acc = np.zeros((natoms,3), dtype=float)
    return atom_pos, atom_vel, atom_acc

def main():
    try:
        prog = sys.argv[0]
    # a = float(sys.argv[1])
    except IndexError:
        # print '\nusage: '+prog+' a (where a is a number)\n'
        sys.exit(0)
    maxRun = 20000
    dt = 0.001
    mass = 1.0079
    ParticleTest = False
    nParticleTest = 4
    c = "string"
    if (ParticleTest == True) and (nParticleTest == 3):
        natoms = 3
        atom_pos, atom_vel, atom_acc = create_arrays(natoms)
        atom_pos[0][0], atom_pos[1][0], atom_pos[2][0] = -2.1, 0.0, +2.1
    elif (ParticleTest == True) and (nParticleTest == 4):
        natoms = 4
        atom_pos, atom_vel, atom_acc = create_arrays(natoms)
        atom_pos[0][0], atom_pos[1][0], atom_pos[2][0], atom_pos[3][0] = -3.1, -1.0, +1.0, +3.1
    else:
        natoms = 10
        atom_pos, atom_vel, atom_acc = create_arrays(natoms)
# initialize
        spacing = 2.1
        for i in range(natoms): # atoms are 2.1 unit apart to start, along the x-axis
            atom_pos[i][0] = i*spacing
            atom_pos[i][1] = i*spacing
# dynamics
    print '# Updating forces in 2D'
    for i in range(maxRun):
        atom_for = update_forces(atom_pos,c)
        atom_acc = update_acc(atom_acc, atom_for, mass)
        atom_vel = update_vel(atom_vel, atom_acc, dt)
        atom_pos = update_pos(atom_pos, atom_vel, dt)
        outstr = ''
     #   distx = dist(atoms_list[i],atoms_list[i-1])
    #    md.write(str(dist))
        for i in range(natoms):
            outstr += str(atom_pos[i][0]) + ' ' + str(atom_pos[i][1]) + ' ' + "0.0" + ' '"\n"
        back.write(outstr + "\n")
        #print outstr
    back.close()
# This executes main() only if executed from shell
if __name__ == '__main__':
    main()
