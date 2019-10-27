#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates a Box
    Inputs:
        origin: The origin (plane) of the torus (list)
        L: the length of the box along X (float)
        W: the width of the box along Y (float)
        H: the height of the box along Z (float)
        fillet_radius: optional fillet radius for the edges (float)
        pts: List of points to query (list)
    Output:
        a: Distance values for all points in pts
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

def get_dist(p,o):
    dx = abs(p.X-o.OriginX) - (L/2-fillet_radius)
    dy = abs(p.Y-o.OriginY) - (W/2-fillet_radius)
    dz = abs(p.Z-o.OriginZ) - (H/2-fillet_radius)
    inside = max(dx,max(dy,dz)) - fillet_radius
    dx = max(dx,0)
    dy = max(dy,0)
    dz = max(dz,0)
    corner = math.pow(dx*dx + dy*dy + dz*dz,0.5) - fillet_radius
    if inside+fillet_radius>0:
        return corner
    else:
        return inside

# set default values
if not L:
    L=5
if not W:
    W=4
if not H:
    H=3
if not fillet_radius:
    fillet_radius = 0

a = [9999.9 for p in pts]
# calculate transformation matrix between worldxy and box plane
voxplane = rs.WorldXYPlane()
for o in origin:
    tpts = [rg.Point3d(p) for p in pts]
    voxplane.Origin = o.Origin
    tf = rg.Transform.PlaneToPlane(o,voxplane)

    # rebase the points according to the transformation matrix
    for p in tpts:
        p.Transform(tf)

    a = [min(a[j],get_dist(p,o)) for j,p in enumerate(tpts)]
