"""Morphs one object into another object.
    Inputs:
        a: first object (sdf)
        b: second object (sdf)
        f: morphing factor, 0: a, 1: b, d=(1-f)*a+f*b
    Output:
        d: the intermediate object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Morph(object):
    def __init__(self,a=None,b=None,f=0.5):
        self.a = a
        self.b = b
        self.f = f

    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        return (1-self.f)*da + self.f*db

if __name__=="__main__":
    if a is not None and b is not None:
        if f is None:
            f = 0.5
        d = Morph(a,b,f)
