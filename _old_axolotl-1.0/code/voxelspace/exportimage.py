#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
exports a layer of the voxel space as an image.
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

from System import Drawing as drw

def get_index(x,y,z):
    return x * nyz + y * nz + z

def get_color(v):
    if v>0:
        col = drw.Color.FromArgb((1 - v / mx) * 255, 127 + (1 - v / mx) * 127, 255)
    else:
        col = drw.Color.FromArgb(255, (1 - v / mn) * 255, 127 + (1 - v / mn) * 127)
    return col


# input check
if not nx:
    nx = 0
if not ny:
    ny = 0
if not nz:
    nz = 0
if not plane:
    plane = 0
if plane>2:
    plane=2
if not level:
    level = 0

nyz = ny*nz
dims = [nz,ny,nx]
if level>=dims[plane]:
    level = dims[plane]-1

mx = max(vals)
mn = min(vals)

if plane==0:
    bmp = drw.Bitmap(nx,ny)
    for x in range(nx):
        for y in range(ny):
            v = vals[get_index(x,y,level)]
            bmp.SetPixel(x,ny-1-y,get_color(v))
elif plane==1:
    bmp = drw.Bitmap(nx,nz)
    for x in range(nx):
        for y in range(nz):
            v = vals[get_index(x,level,y)]
            bmp.SetPixel(x,nz-1-y,get_color(v))
elif plane==2:
    bmp = drw.Bitmap(ny,nz)
    for x in range(ny):
        for y in range(nz):
            v = vals[get_index(level,x,y)]
            bmp.SetPixel(x,nz-1-y,get_color(v))

plids = ['XY','XZ','YZ']
drw.Bitmap.Save(bmp,path+"cplane_"+str(plids[plane])+"_layer_"+str(level)+".png")
