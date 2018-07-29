# -*- coding: utf-8 -*-

"""
Creates a metaball object around the points in center.
Either one weight for all or one for each point can be specified.
Negative weights result in repulsion.
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
    d = 0
    # sum all the weights over distance squared
    for i,e in enumerate(center):
        d += weight[i]/sum((p[j]-e[j])**2 for j in range(3))
    return -d+0.8

if __name__ == "__main__":
    # check inputs
    if not weight:
        weight = [50.0 for _ in center]
    if len(weight)<len(center):
        weight = [weight[0] for _ in center]

    a = [get_dist(p) for p in pts]
