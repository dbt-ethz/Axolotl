#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates a shell from the solid object.
    Inputs:
        vals: field values
        thickness: thickness of shell
        side: 0=outside, 1=inside, 0.5=half/half
    Output:
        a: new field values
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

# input check
if not thickness:
    thickness = 1
if not side:
    side = 0.5

a = [abs(v + (side-0.5)*thickness) - thickness/2 for v in vals]
