import numpy as np
from matplotlib import pyplot
import time,sys

nx = 41         #Number of gridpoints
dx =2/(nx-1)    #distance between any pair of adjacent grid points
nt = 25         #Number of timesteps
dt = .025       #dt is the amount of time each step covers
c =1            #assume wavespeed =1

# Set up initial conditions
#u =2 in the interval 0.5<= x<=1
# u = 1 in the interval everywhere else (0,2)

u = np.ones(nx) #1-d Array filled with only ones of size 41
u[int(0.5/dx):int(1/ dx + 1)] = 2     #setting u = 2 between 0.5 to 1
#print(u)        #print u values

#pyplot.plot(np.linspace(0,2,nx),u);
#pyplot.show()   #showcasing the values

## For every value of u we need to apply the finite-difference scheme (FTCS)?? Not sure if thats the right one

un = np.ones(nx)    #initializing a temp array

for n in range(nt):     #loop for all vals of n from 0 to nt(Number of timesteps)
    un = u.copy()
    for i in range(1,nx):
        u[i]=un[i] - c * dt/dx * (un[i]-un[i-1])


print(u)
pyplot.plot(np.linspace(0,2,nx),u)
pyplot.show()
