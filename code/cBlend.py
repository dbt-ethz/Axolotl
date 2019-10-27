"""Creates a smooth blend union.
    Inputs:
        a: first sdf object
        b: second sdf object
        f: smoothing factor (default 2.0)
    Output:
        d: the blend object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Blend(object):
    """
    smooth blend between a and b
    """
    def __init__(self, obja, objb, r=2.0):
        self.a = obja
        self.b = objb
        self.r = r

    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        e = max(self.r - abs(da-db), 0)
        return min(da,db) - e*e*0.25/self.r

if __name__=="__main__":
    if a is not None and b is not None:
        if f is None:
            f = 2.0
        d = Blend(a,b,f)
