"""Creates a distance field from a mesh.
If the mesh is closed, points inside will return negative values.
    Inputs:
        m: the mesh
    Output:
        d: the mesh object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

class Mesh(object):

    def __init__(self,m=None):
        self.m = m

    def get_distance(self,x,y,z):
        p = rg.Point3d(x,y,z)
        cp = rs.MeshClosestPoint(self.m,p)
        d = rs.Distance(p,cp[0])
        bln = self.m.IsPointInside(p,0.1,False)
        if bln:
            d *= -1
        return d


if __name__=="__main__":
    if not m is None:
        d = Mesh(m)
