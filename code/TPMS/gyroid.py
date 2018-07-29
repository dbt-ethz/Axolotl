#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
TPMS: Gyroid
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import math

def get_val(p):
    px = p.X/fact
    py = p.Y/fact
    pz = p.Z/fact
    v = (
        math.sin(px)*math.cos(py) +
        math.sin(py)*math.cos(pz) +
        math.sin(pz)*math.cos(px))
    return v

# input check
if not wavelength:
    wavelength = math.pi

fact = wavelength/math.pi

a = [get_val(p) for p in pts]
