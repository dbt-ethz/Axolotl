#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates circular pipes along one or multiple curve(s).
If only one radius is specified, it is used for all the curves.
If no end radius is specified, the start radius is used.
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import math

def map_values(input_val, in_from, in_to, out_from, out_to):
    out_range = out_to - out_from
    in_range = in_to - in_from
    in_val = input_val - in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val

def get_dist(p,j):
    param=rs.CurveClosestPoint(axis[j], p)
    cp=rs.EvaluateCurve(axis[j],param)
    dv = map_values(param,axis[j].Domain[0],axis[j].Domain[1],0,1)
    r = (1-dv)*start_radius[j] + dv*end_radius[j]
    d = rs.Distance(p,cp) - r
    return d

if __name__ == "__main__":
    # check inputs
    if not start_radius:
        start_radius = [5.0 for _ in axis]
    if not end_radius:
        end_radius = [r for r in start_radius]
    if len(start_radius)<len(axis):
        start_radius = [start_radius[0] for _ in axis]
    if len(end_radius)<len(axis):
        end_radius = [end_radius[0] for _ in axis]

    # calculate distances
    a = [9999.9 for p in pts]
    for j,c in enumerate(axis):
        a = [min(a[i],get_dist(p,j)) for i,p in enumerate(pts)]
