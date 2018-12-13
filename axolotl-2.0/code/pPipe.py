"""Creates a pipe along a curve.
    Inputs:
        c: the axis curve
        r1: radius at the start of the curve
        r2: radius at the end of the curve
    Output:
        d: the pipe object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

def map_values(input_val, in_from, in_to, out_from, out_to):
    out_range = out_to - out_from
    in_range = in_to - in_from
    in_val = input_val - in_from
    val=(float(in_val)/in_range)*out_range
    out_val = out_from+val
    return out_val

class Pipe(object):

    def __init__(self,c=None,r1=1.0,r2=1.0):
        self.c = c
        self.r1 = r1
        self.r2 = r2

    def get_distance(self,x,y,z):
        p = rs.CreatePoint(x,y,z)
        param=rs.CurveClosestPoint(self.c, p)
        cp=rs.EvaluateCurve(self.c,param)
        dv = map_values(param,self.c.Domain[0],self.c.Domain[1],0,1)
        r = (1-dv)*self.r1 + dv*self.r2
        d = rs.Distance(p,cp) - r
        return d

if __name__=="__main__":
    if len(c)>0:
        if r1 is None:
            r1 = 1.0
        if r2 is None:
            r2 = 1.0

        if len(c)>1:
            d = [Pipe(t,r1,r2) for t in c]
        else:
            d = Pipe(c[0],r1,r2)
