# -*- coding: utf-8 -*-

"""
Creates one or multiple Sphere(s)
If multiple centers and one radius is fed in, all spheres are created with equal radius.
If only one center but multiple radii are fed in, only the biggest sphere is created (others are within).
If multiple centers and multiple radii are fed in, values are matched by index (shorter list).
    Inputs:
        center: The center(s) of the sphere(s) (list)
        radius: The radius/radii for the sphere(s) (list)
        pts: List of points to query (list)
    Output:
        a: Distance values for all points in pts
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs

if not radius:
    radius = [10]
if not center:
    center = [(0,0,0)]

# with multiple centers and only one radius,
# all spheres get the same radius
if len(radius)==1 and len(center)>1:
    radius = [radius[0] for _ in center]

# with only one center and multiple radii,
# only the biggest radius is considered
if len(center)==1 and len(radius)>1:
    radius = [max(radius)]

if len(radius) != len(center):
    num = min(len(radius),len(center))
    radius = radius[:num]
    center = center[:num]

a = [9999 for p in pts]
for i,c in enumerate(center):
    a = [min(a[j],rs.Distance(c,p)-radius[i]) for j,p in enumerate(pts)]
