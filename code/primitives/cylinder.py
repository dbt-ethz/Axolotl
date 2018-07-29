#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates cylinders centered aroung the origin planes.
If only one radius is specified, it is used for all the cylinders.
If only one height is specified, it is used for all the cylinders.
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

def get_dist(p,o,r,h):
    dx = abs(p.X-o.OriginX)
    dy = abs(p.Y-o.OriginY)
    dz = abs(p.Z-o.OriginZ)

    d = math.sqrt(dx*dx + dy*dy) - r
    d = max(d, abs(dz) - h/2)
    return d

# check inputs
if not radius:
    radius = [5.0 for _ in origin]
if not height:
    height = [15.0 for _ in origin]
if len(radius)<len(origin):
    radius = [radius[0] for _ in origin]
if len(height)<len(origin):
    height = [height[0] for _ in origin]

# calculate transformation matrix between worldxy and box plane
voxplane = rs.WorldXYPlane()
a = [9999.9 for p in pts]
for i,o in enumerate(origin):
    tpts = [rg.Point3d(p) for p in pts]
    voxplane.Origin = o.Origin
    tf = rg.Transform.PlaneToPlane(o,voxplane)

    # rebase the points according to the transformation matrix
    for p in tpts:
        p.Transform(tf)

    a = [min(a[j],get_dist(p,o,radius[i],height[i])) for j,p in enumerate(tpts)]
