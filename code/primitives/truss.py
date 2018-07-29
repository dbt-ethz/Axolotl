#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates a network of pipes around a list of lines.
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs

def get_dist(p):
    co = rs.PointClosestObject(p,lines)
    d = rs.Distance(p,co[1])
    return d - radius

# input check
if not radius:
    radius = 5

a = [get_dist(p) for p in pts]
