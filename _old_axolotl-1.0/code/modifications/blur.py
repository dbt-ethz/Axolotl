#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
adds blur to the field (Gaussian kernel)
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import math

if not radius:
    radius = 3

if not nx:
    nx = 0
if not ny:
    ny = 0
if not nz:
    nz = 0

nyz = ny*nz
nxy = nx*ny
kernelsize = 1+radius*2
kernel = [0 for _ in range(kernelsize)]
sigma = radius/3.0
sigmasqr = sigma*sigma*2.0
factor = 1.0/sigma * math.sqrt(2*math.pi)

sumkernel = 0
for i in xrange(kernelsize):
    distance = radius - i
    kernel[i] = factor * math.exp(-distance*distance/sigmasqr)
    sumkernel += kernel[i]

kernel = [v/sumkernel for v in kernel]

a = [0.0 for _ in vals]

ix = 0
for x in xrange(nx):
    for y in xrange(ny):
        for z in xrange(nz):
            sumv = 0.0
            for i,v in enumerate(kernel):
                cx = x+i-radius
                if cx>=0 and cx<nx:
                    tix = cx*nyz+y*nz+z
                    #tix = cx+y*nx+z*nxy
                    sumv += vals[tix]*v
            a[ix] += sumv
            ix += 1

ix = 0
for x in xrange(nx):
    for y in xrange(ny):
        for z in xrange(nz):
            sumv = 0.0
            for i,v in enumerate(kernel):
                cy = y+i-radius
                if cy>=0 and cy<ny:
                    tix = x*nyz+cy*nz+z
                    #tix = x+cy*nx+z*nxy
                    sumv += vals[tix]*v
            a[ix] += sumv
            ix += 1

ix = 0
for x in xrange(nx):
    for y in xrange(ny):
        for z in xrange(nz):
            sumv = 0.0
            for i,v in enumerate(kernel):
                cz = z+i-radius
                if cz>=0 and cz<nz:
                    tix = x*nyz+y*nz+cz
                    #tix = x+y*nx+cz*nxy
                    sumv += vals[tix]*v
            a[ix] += sumv
            ix += 1

a = [v/3.0 for v in a]
