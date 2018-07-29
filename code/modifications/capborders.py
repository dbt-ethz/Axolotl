#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
caps the voxel space borders to create a closed mesh
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs

def get_index(x,y,z):
    return x * nyz + y * nz + z

# input check
if not nx:
    nx = 0
if not ny:
    ny = 0
if not nz:
    nz = 0

nyz = ny * nz
a = [d for d in vals]
val = 99999.9

for u in range(nx):
    for v in range(ny):
        ia = get_index(u,v,0)
        ib = get_index(u,v,nz-1)
        a[ia] = val
        a[ib] = val

for v in range(ny):
    for w in range(nz):
        ia = get_index(0,v,w)
        ib = get_index(nx-1,v,w)
        a[ia] = val
        a[ib] = val

for w in range(nz):
    for u in range(nx):
        ia = get_index(u,0,w)
        ib = get_index(u,ny-1,w)
        a[ia] = val
        a[ib] = val
