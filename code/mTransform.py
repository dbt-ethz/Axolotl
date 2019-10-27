"""Applies a matrix transformation to an object.
    Inputs:
        x: the sdf object to be transformed
        m: the 4x4 transformation matrix (e.g. translation, rotation, shear...)
    Output:
        d: the transformed object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

class Transform(object):
    def __init__(self,o=None,m=None):
        self.o = o
        self.m = m
        success, self.orig = self.m.TryGetInverse()

    def get_distance(self,x,y,z):
        p = rg.Point3f(x,y,z)
        p.Transform(self.orig)
        return self.o.get_distance(p.X,p.Y,p.Z)

if __name__=="__main__":
    if x is not None:
        if m is None:
            m = rg.Transform.Identity
        d = Transform(x,m)
