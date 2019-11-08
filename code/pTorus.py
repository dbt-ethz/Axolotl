"""Creates a torus.
    Inputs:
        r1: radius of the donut
        r2: radius of the pipe
        p: plane of origin
    Output:
        d: the torus object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

class Torus(object):
    """
    this is the torus class
    """
    def __init__(self, r1=2, r2=1):
        self.r1 = r1
        self.r2 = r2
        self.plane = None
        self.transform = None

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
            dx, dy, dz = x, y, z

        dxy = math.sqrt(dx**2 + dy**2)
        d2 = math.sqrt((dxy-self.r1)**2 + dz**2)
        d = d2-self.r2

        return d

if __name__=="__main__":
    if r1 is None:
        r1 = 1.5
    if r2 is None:
        r2 = 1.0
    d = Torus(r1,r2)
    if p is not None:
        d.set_plane(p)
