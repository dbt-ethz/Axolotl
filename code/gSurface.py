"""Creates an SDF by thickening a surface.
    Inputs:
        s: the surface
        t: the thickness (half on either side)
    Output:
        d: the surface object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Surface(object):

    def __init__(self,s=None,t=1.0):
        self.s = s
        self.t = t

    def get_distance(self,x,y,z):
        p = rs.CreatePoint(x,y,z)
        param = rs.SurfaceClosestPoint(self.s, p)
        cp = rs.EvaluateSurface(self.s, param[0],param[1])
        d = rs.Distance(p,cp)-self.t/2.0
        return d


if __name__=="__main__":
    if t is None:
        t = 1.0
    if s is not None:
        d = Surface(s,t)
        print(d.get_distance(0,0,2))
