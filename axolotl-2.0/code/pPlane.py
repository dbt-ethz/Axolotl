"""Creates a series of planes.
    Inputs:
        n: list of normal vectors
        o: offset distance from the origin
    Output:
        d: the plane object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

class Plane(object):
    """
    this is the plane class
    """
    def __init__(self, nx=0, ny=0, nz=1, dst=0):
        self.nrm = rg.Vector3f(nx,ny,nz)
        self.nrm.Unitize()
        self.d = dst

    def get_distance(self,x,y,z):
        dp = rs.VectorDotProduct(self.nrm, rg.Vector3d(x,y,z))
        return - (dp+self.d)

if __name__=="__main__":
    if o is None:
        o = 0.0
    if len(n)>1:
        d = [Plane(t.X,t.Y,t.Z,o) for t in n]
    elif len(n)==1:
        d = Plane(n[0].X,n[0].Y,n[0].Z,o)
    else:
        n = rg.Vector3f(0,0,1)
        d = Plane(n.X,n.Y,n.Z,o)
