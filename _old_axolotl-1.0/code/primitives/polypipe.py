#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
extrudes a star polygon along a curve
Inputs:
    axis: the axis curve
    n : the number of points in the polygon (doubles when star)
    r : the radius of the polygon
    r2 : second radius to create a star polygon
    sa : rotation angle at start (0 if omitted)
    ea : rotation angle at end (same as sa if omitted)
    pts: List of points to query (list)
Output:
    a: Distance values for all points in pts
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

# check input
if not n:
	n=6
if n<3:
	n=3
if not r:
	r = 10
if r<0:
	r = math.abs(r)
if not sa:
    sa = 0
if not ea:
    ea = sa

if r2:
	n*=2

def get_dist(pt,poly):
    # find closest point on axis curve
    param = rs.CurveClosestPoint(axis, pt)
    # get plane perpendicular to curve
    ck,pl = axis.PerpendicularFrameAt(param)
    # part responsible for flat end caps
    # if distance from point to plane is bigger than 0,
    # return that distance
    pp = rs.PlaneClosestPoint(pl,pt)
    d2 = rs.Distance(pt,pp)
    if d2>0.01:
        return d2

    # else change the basis of the polygon from world xy
    # to that plane to check for distance and inside/outside
    pm = (param-axis.Domain[0])/(axis.Domain[1]-axis.Domain[0])

    wxy = rs.WorldXYPlane()
    tf = rg.Transform.PlaneToPlane(wxy,pl)
    ang = sa + pm*(ea-sa)
    tr = rg.Transform.Rotation(ang, pl.Normal, pl.Origin)
    tpts = rs.CurvePoints(poly)
    for p in tpts:
        p.Transform(tf)
        p.Transform(tr)
    ply = rs.AddPolyline(tpts)
    prm = rs.CurveClosestPoint(ply,pt)
    cp = rs.EvaluateCurve(ply,prm)
    d = rs.Distance(pt,cp)
    # if the point is inside the curve, reverse the distance
    bln = rs.PointInPlanarClosedCurve(pt,ply,pl)
    if bln:
        d *= -1
    return d

def get_polygon():
	ai = 2*math.pi / n
	plpts = []
	for s in range(n+1):
		if r2:
			rt = ((s+1)%2)*r+(s%2)*r2
		else:
			rt = r
		x = rt * math.cos(s*ai)
		y = rt * math.sin(s*ai)
		plpts.append(rg.Point3d(x,y,0))
	return rs.AddPolyline(plpts)

ply = get_polygon()

a = [get_dist(p,ply) for p in pts]
