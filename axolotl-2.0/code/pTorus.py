"""Creates a torus.
    Inputs:
        r1: radius of the donut
        r2: radius of the pipe
    Output:
        d: the torus object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
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
        self.loc = rg.Vector3f(0,0,0)
        self.r1 = r1
        self.r2 = r2

    def get_distance(self,x,y,z):
        """
        distance function
        """
        dx = x-self.loc.X
        dy = y-self.loc.Y
        dz = z-self.loc.Z

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
