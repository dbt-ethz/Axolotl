"""Creates a twist around the normal of a specified plane.
    Inputs:
        x: the solid sdf object to be twisted
        a: the twist angle per distance from plane p
        p: the plane around which's normal to twist
    Output:
        d: the twist object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

class Twist(object):
    def __init__(self,obj=None, ang=0.0, plane=None):
        self.o = obj
        self.angle = float(ang)
        self.plane = plane
        worldxy = rg.Plane.WorldXY
        self.transform = rg.Transform.PlaneToPlane(self.plane, worldxy)
        success, self.inverse = self.transform.TryGetInverse()

    def get_distance(self,x,y,z):
        p = rg.Point3d(x,y,z)
        p.Transform(self.transform)
        t = p.Z
        theta = t * self.angle
        nx = (p.X * math.cos(theta) - p.Y * math.sin(theta))
        ny = (p.X * math.sin(theta) + p.Y * math.cos(theta))
        pi = rg.Point3d(nx,ny,p.Z)
        pi.Transform(self.inverse)
        return self.o.get_distance(pi.X, pi.Y, pi.Z)

if __name__=="__main__":
    if x is not None:
        if a is None:
            a = 1.0
        if p is None:
            p = rg.Plane.WorldXY
        d = Twist(x, a, p)
