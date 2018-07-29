#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Creates a distance field from a mesh.
If the mesh is closed, values inside are negative, values outside are positive.
For open meshes, all distances are positive, zero for points on the mesh.
To thicken an open mesh, subtract half the desired thickness before creating the isosurface.
"""
__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

def get_dist(p):
	cp=rs.MeshClosestPoint(mesh,p)
	d = rs.Distance(p,cp[0])
	bln = mesh.IsPointInside(p,0.1,False)
	if bln:
		d *= -1
	return d

a = [get_dist(p) for p in pts]
