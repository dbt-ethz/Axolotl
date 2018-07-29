#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates a distance field from a NURBS surface with a specific thickness
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

def get_dist(p):
    param=rs.SurfaceClosestPoint(surf, p)
    cp=rs.EvaluateSurface(surf, param[0],param[1])
    #n = rs.SurfaceNormal(surf,param)
    #dv = map_values(param,axis.Domain[0],axis.Domain[1],0,1)
    #r = (1-dv)*start_radius + dv*end_radius
    d = rs.Distance(p,cp)-thickness/2.0
    return d

if __name__ == '__main__':
    a = [get_dist(p) for p in pts]
