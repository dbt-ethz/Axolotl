#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates a spatial lattice truss in a predefined cube.
    Inputs:
        nx: The x-dimension of the original voxel space to fill
        ny: The y-dimension of the original voxel space to fill
        nz: The z-dimension of the original voxel space to fill
        n: The number of voxels along one side of the cube cell
        r: The ratio between diameter and n (0 to 1)
        mode: type of lattice (see code). more can easily be added as list of lists (point pair)
    Output:
        a: Distance values for all points in voxel space (nx, ny, nz)
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

if nx==None:
    nx = 30
if ny==None:
    ny = 30
if nz==None:
    nz = 30
if n==None:
    n=15
if r==None:
    r = 0.15
if mode==None:
    mode=0
if mode<0 or mode>9:
    mode=0
def dot(i,j,k,l,m,n):
    return i*l + j*m + k*n

def get_dist(p,ls,le):
    x = p.X
    y = p.Y
    z = p.Z

    x1 = ls[0]
    y1 = ls[1]
    z1 = ls[2]

    x2 = le[0]
    y2 = le[1]
    z2 = le[2]

    vx = x2-x1
    vy = y2-y1
    vz = z2-z1
    c2 =  dot(vx, vy, vz, vx, vy, vz)

    dx = x - x1
    dy = y - y1
    dz = z - z1
    c1 =  dot(dx, dy, dz, vx, vy, vz)

    b = c1 / c2
    px = x1 + b * vx
    py = y1 + b * vy
    pz = z1 + b * vz

    d = math.sqrt((x-px)**2 + (y-py)**2 + (z-pz)**2)
    return d - f

def get_index(x,y,z):
    return x * nyz + y * nz + z

def get_local_ix(x,y,z):
    return x*n**2 + y*n + z

rx = int(nx/n)+1
ry = int(ny/n)+1
rz = int(nz/n)+1
nyz = ny*nz

f = n*r/2

v1 = 0.0
v2 = 0.5 * n
v3 = v2/2

loc = [[]]*20

loc[0] = [v1,v1,v1]
loc[1] = [v2,v1,v1]
loc[2] = [v2,v2,v1]
loc[3] = [v1,v2,v1]

loc[4] = [v1,v1,v2]
loc[5] = [v2,v1,v2]
loc[6] = [v2,v2,v2]
loc[7] = [v1,v2,v2]

loc[8]  = [v3,v1,v1]
loc[9]  = [v2,v3,v1]
loc[10] = [v3,v2,v1]
loc[11] = [v1,v3,v1]

loc[12] = [v1,v1,v3]
loc[13] = [v2,v1,v3]
loc[14] = [v2,v2,v3]
loc[15] = [v1,v2,v3]

loc[16] = [v3,v1,v2]
loc[17] = [v2,v3,v2]
loc[18] = [v3,v2,v2]
loc[19] = [v1,v3,v2]

bigx = [[loc[0],loc[6]]]
grid = [[loc[6],loc[2]],[loc[6],loc[5]],[loc[6],loc[7]]]
star = grid + bigx
cross = [[loc[1],loc[6]],[loc[3],loc[6]],[loc[4],loc[6]]]
octagon = [[loc[1],loc[3]],[loc[3],loc[4]],[loc[4],loc[1]]]
octet = cross + octagon
vintile = [[loc[8],loc[13]],[loc[13],loc[17]],[loc[17],loc[18]],[loc[18],loc[15]],[loc[15],loc[11]],[loc[11],loc[8]]]
dual = [[loc[0],loc[1]],[loc[0],loc[3]],[loc[0],loc[4]]]
interlock = grid+dual
isotrop = [[loc[0],loc[1]],[loc[2],loc[1]],[loc[5],loc[1]],[loc[7],loc[1]],[loc[3],loc[7]],[loc[6],loc[7]],[loc[4],loc[7]]]

lines = grid

if mode==0:
    lines = octet
elif mode==1:
    lines = bigx
elif mode==2:
    lines = grid
elif mode==3:
    lines = star
elif mode==4:
    lines = cross
elif mode==5:
    lines = octagon
elif mode==6:
    lines = vintile
elif mode==7:
    lines = dual
elif mode==8:
    lines = interlock
elif mode==9:
    lines = isotrop

a = [9999] * (nx*ny*nz)
b = [0]*(n**3)

off = 0.5 + (n%2)*0.5

nn = int(round(n/2.0))
for x in range(nn):
    for y in range(nn):
        for z in range(nn):
            p = rg.Point3d(nn-x - off,nn-y - off,nn-z - off)
            v = 99999
            for l in lines:
                v = min(v,get_dist(p,l[0],l[1]))
            b[get_local_ix(x,y,z)] = v
            b[get_local_ix(n-x-1,y,z)] = v
            b[get_local_ix(x,n-y-1,z)] = v
            b[get_local_ix(x,y,n-z-1)] = v
            b[get_local_ix(n-x-1,n-y-1,z)] = v
            b[get_local_ix(x,n-y-1,n-z-1)] = v
            b[get_local_ix(n-x-1,y,n-z-1)] = v
            b[get_local_ix(n-x-1,n-y-1,n-z-1)] = v

for i in range(rx):
    for j in range(ry):
        for k in range(rz):
            #maybe try to replace these following 3 for loops with a clever slicing [:,xy]
            for x in range(n):
                for y in range(n):
                    for z in range(n):
                        ix = i*n+x
                        iy = j*n+y
                        iz = k*n+z
                        if ix<nx and iy<ny and iz<nz:
                            a[get_index(ix,iy,iz)] = b[get_local_ix(x,y,z)]
