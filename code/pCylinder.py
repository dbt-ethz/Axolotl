"""Creates a cylinder.
    Inputs:
        r: radius of the cylinder
        h: height of the cylinder
        p: plane of origin
    Output:
        d: the cylinder object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

class Cylinder(object):
    """
    this is the cylinder class
    """
    def __init__(self, r=1, h=1):
        self.loc = rg.Vector3f(0,0,0)
        self.plane = None
        self.transform = None
        self.r = r
        self.h = h

    def set_plane(self, p):
        self.plane = p
        matrix = rg.Transform.PlaneToPlane(rg.Plane.WorldXY, self.plane)
        success, self.transform = matrix.TryGetInverse()

    def get_distance(self,x,y,z):
        """
        distance function
        """
        if self.transform is not None:
            p = rg.Point3f(x,y,z)
            p.Transform(self.transform)
            dx = p.X
            dy = p.Y
            dz = abs(p.Z)
        else:
            dx, dy, dz = x, y, abs(z)

        # 2d circle distance
        dxy = math.sqrt(dx**2 + dy**2) - self.r
        # cut with cap plances
        d = max(dxy, dz-self.h/2.0)
        return d

if __name__=="__main__":
    if r is None:
        r = 1.0
    if h is None:
        h = 2.0
    d = Cylinder(r,h)
    if p is not None:
        d.set_plane(p)
