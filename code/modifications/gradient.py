"""
Calculates a gradient direction vector for every cell.
    Inputs:
        vals: distance field values
        nx: number of cells in x direction
        ny: number of cells in y direction
        nz: number of cells in z direction
    Output:
        a: a 3d vector in gradient direction for every cell
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import Rhino.Geometry as rg

a = []

nyz = ny*nz

def get_index(x,y,z):
    return x*nyz + y*nz + z

for x in range(nx):
    for y in range(ny):
        for z in range(nz):
            if x==0 or x==nx-1 or y==0 or y==ny-1 or z==0 or z==nz-1:
                a.append(rg.Vector3d(0,0,0))
            else:
                ux = vals[get_index(x-1,y,z)]
                vx = vals[get_index(x+1,y,z)]
                uy = vals[get_index(x,y-1,z)]
                vy = vals[get_index(x,y+1,z)]
                uz = vals[get_index(x,y,z-1)]
                vz = vals[get_index(x,y,z+1)]
                a.append(rg.Vector3d(vx-ux,vy-uy,vz-uz))
