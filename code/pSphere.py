"""Creates a sphere.
    Inputs:
        r: sphere radius
        c: center point
    Output:
        d: the sphere object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

class Sphere(object):
    """
    this is the box class
    """
    def __init__(self, r=0):
        self.loc = rg.Point3f(0,0,0)
        self.r = r

    def get_distance(self,x,y,z):
        """
        distance function
        """
        # long version
        d = math.sqrt((x-self.loc.X)**2 + (y-self.loc.Y)**2 + (z-self.loc.Z)**2) - self.r

        return d


if __name__=="__main__":
    if r is None:
        r = 1
    d = Sphere(r)
    if c is not None:
        d.loc = c
