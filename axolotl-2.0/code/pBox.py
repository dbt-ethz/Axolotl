"""Creates a box with an optional edge fillet.
    Inputs:
        a: length along the x axis
        b: length along the y axis
        c: length along the z axis
        r: edge fillet radius
    Output:
        d: the box object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

class RBox(object):
    """
    this is the box class
    """
    def __init__(self, a=1, b=1, c=1, r=0):
        self.loc = rg.Vector3f(0,0,0)
        #self.loc = Vector(0,0,0)
        self.a = a
        self.b = b
        self.c = c
        self.r = r

    def get_distance(self,x,y,z):
        """
        distance function
        """
        dx = abs(x-self.loc.X)-(self.a/2.0-self.r)
        dy = abs(y-self.loc.Y)-(self.b/2.0-self.r)
        dz = abs(z-self.loc.Z)-(self.c/2.0-self.r)
        inside = max([dx,dy,dz])-self.r
        dx = max(dx,0)
        dy = max(dy,0)
        dz = max(dz,0)
        if inside+self.r>0:
            #rounded corner case
            return math.sqrt(dx**2 + dy**2 + dz**2) - self.r
        else:
            return inside

    def get_bounds(self):
        return (self.loc.X-self.a/2.0, self.loc.Y-self.b/2.0, self.loc.Z-self.c/2.0,
                self.loc.X+self.a/2.0, self.loc.Y+self.b/2.0, self.loc.Z+self.c/2.0)

if __name__=="__main__":
    if a is None:
        a = 2
    if b is None:
        b = 3
    if c is None:
        c = 4
    if r is None:
        r = 0
    d = RBox(a,b,c,r)
