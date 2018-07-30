#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
gradient vectors from voxelspace
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

nyz = ny*nz
nxy = nx*ny

print nx,ny,nz

def get_index(x,y,z):
    return x * nyz + y * nz + z

a = []
b = []

for x in range(nx):
    for y in range(ny):
        for z in range(nz//2,nz//2+1):
            b.append(rg.Vector3d(3*x-100,3*y-100,3*z-100))
            if x==0 or x==nx-1 or y==0 or y==ny-1 or z==0 or z==nz-1:
                a.append(rg.Vector3d(0,0,0))
            else:
                ix = get_index(x,y,z)
                v = vals[ix]

                xx = get_index(x+1,y,z)
                vx = vals[xx]
                xx = get_index(x-1,y,z)
                ux = vals[xx]

                yy = get_index(x,y+1,z)
                vy = vals[yy]
                yy = get_index(x,y-1,z)
                uy = vals[yy]

                zz = get_index(x,y,z+1)
                vz = vals[zz]
                zz = get_index(x,y,z-1)
                uz = vals[zz]

                a.append(rg.Vector3d(vy-uy,-1*(vx-ux),vz-uz))
