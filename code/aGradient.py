"""Calculates the gradient vector for every p in pts. ∇f(p)
as described here: https://www.iquilezles.org/www/articles/normalsSDF/normalsSDF.htm
    Inputs:
        x: the sdf object used for distance calculation
        pts: a list of points for which to calculate the gradient
        e: epsilon, the offset distance from p to calculate central difference
    Output:
        a: a list of 3d vectors for each point in pts"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2019 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

def get_gradient(p):
    gx = x.get_distance(p.X+e,p.Y,p.Z) - x.get_distance(p.X-e,p.Y,p.Z)
    gy = x.get_distance(p.X,p.Y+e,p.Z) - x.get_distance(p.X,p.Y-e,p.Z)
    gz = x.get_distance(p.X,p.Y,p.Z+e) - x.get_distance(p.X,p.Y,p.Z-e)
    v = rs.CreateVector(gx,gy,gz)
    v.Unitize()
    return v

if __name__=='__main__':
    a = [get_gradient(p) for p in pts]
