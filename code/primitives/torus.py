# -*- coding: utf-8 -*-

"""
Creates a Torus
    Inputs:
        origin: The origin (plane) of the torus (list)
        radius_a: Radius from center to axis (float)
        radius_b: Radius of pipe around axis (float)
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

# the distance function
def get_dist(p,o):
    lxy = math.sqrt(math.pow(o.OriginX-p.X,2) + math.pow(o.OriginY-p.Y,2))
    l2  = math.sqrt(math.pow(lxy-radius_a,2) + math.pow(o.OriginZ-p.Z,2))
    return l2-radius_b

# input check
if not radius_a:
    radius_a = 10
if not radius_b:
    radius_b = 5

a = [9999.9 for p in pts]
voxplane = rs.WorldXYPlane()
for o in origin:
    tpts = [rg.Point3d(p) for p in pts]
    voxplane.Origin = o.Origin
    tf = rg.Transform.PlaneToPlane(o,voxplane)

    # rebase the points according to the transformation matrix
    for p in tpts:
        p.Transform(tf)

    # calculate distance for each point
    a = [min(a[j],get_dist(p,o)) for j,p in enumerate(tpts)]
