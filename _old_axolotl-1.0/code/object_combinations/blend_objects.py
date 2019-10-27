#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
adds two objects A and B with a smooth blend, using an exponential function.
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import math

a = []
# input check
if not A:
    A = []
if not B:
    B = []
if not k:
    k = 0.1

# combine values A and B into new list
for t in zip(A,B):
    v1 = t[0]
    v2 = t[1]
    res = math.exp(-k*v1) + math.exp(-k*v2)
    vr = -math.log(max(0.000001,res))/k
    a.append(vr)
