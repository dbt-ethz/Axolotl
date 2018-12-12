"""Creates a cylinder.
    Inputs:
        r: radius of the cylinder
        h: height of the cylinder
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
        self.r = r
        self.h = h

    def get_distance(self,x,y,z):
        """
        distance function
        """
        dx = x-self.loc.X
        dy = y-self.loc.Y
        dz = abs(z-self.loc.Z)

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
