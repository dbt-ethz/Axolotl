#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
creates different platonic solids as generalized distance function (GDF)
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

"""
GDF for Generalized Distance Function, see here for paper:
    https://www.viz.tamu.edu/faculty/ergun/research/implicitmodeling/papers/sm99.pdf
"""

import math
import Rhino.Geometry as rg

if not center:
    center = rg.Point3d(0,0,0)

if not radius:
    radius = 5

if not type:
    type = 0

if not e:
    e = 32.0

stix = 0
enix = 0

if type>4 or type<0:
    type = 0

if type==0: # dodecahedron
    stix = 13
    enix = 18
if type==1: # octahedron
    stix = 3
    enix = 6
if type==2: # icosahedron
    stix = 3
    enix = 12
if type==3: # truncated octahedron
    stix = 0
    enix = 6
if type==4: # truncated icosahedron
    stix = 3
    enix = 18

# PHI = math.sqrt(5.0)*0.5+0.5
va = 0.577
vb = 0.357
vc = 0.943
vd = 0.851
ve = 0.526
gdf_vectors = []
gdf_vectors.append(rg.Vector3d(1,0,0))
gdf_vectors.append(rg.Vector3d(0,1,0))
gdf_vectors.append(rg.Vector3d(0,0,1))

gdf_vectors.append(rg.Vector3d(va,va,va))
gdf_vectors.append(rg.Vector3d(-va,va,va))
gdf_vectors.append(rg.Vector3d(va,-va,va))
gdf_vectors.append(rg.Vector3d(va,va,-va))

gdf_vectors.append(rg.Vector3d(0,vb,vc))
gdf_vectors.append(rg.Vector3d(0,-vb,vc))
gdf_vectors.append(rg.Vector3d(vc,0,vb))
gdf_vectors.append(rg.Vector3d(-vc,0,vb))
gdf_vectors.append(rg.Vector3d(vb,vc,0))
gdf_vectors.append(rg.Vector3d(-vb,vc,0))

gdf_vectors.append(rg.Vector3d(0,vd,ve))
gdf_vectors.append(rg.Vector3d(0,-vd,ve))
gdf_vectors.append(rg.Vector3d(ve,0,vd))
gdf_vectors.append(rg.Vector3d(-ve,0,vd))
gdf_vectors.append(rg.Vector3d(vd,ve,0))
gdf_vectors.append(rg.Vector3d(-vd,ve,0))

def get_dist(p):
    d = 0.0
    for i in range(stix,enix+1):
        dp = rg.Vector3d.Multiply(p-center,gdf_vectors[i])
        d += math.pow(abs(dp), e)

    d = math.pow(d, 1.0/e) - radius

    return d

a = [get_dist(p) for p in pts]
