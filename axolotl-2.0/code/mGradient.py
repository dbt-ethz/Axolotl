"""Creates a gradient by adding a fraction of object b to object a.
    Inputs:
        a: the base sdf object (modified)
        b: the object to be added (modifier)
        f: intensity factor (d = a + f * b), default: 0.01
    Output:
        d: the modified object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Gradient(object):
    """
    modifies obj a with a fraction (f) of obj b
    """
    def __init__(self, obja, objb, f=0.1):
        self.a = obja
        self.b = objb
        self.f = f

    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        return da+self.f*db

if __name__=="__main__":
    if a is not None and b is not None:
        if f is None:
            f = 0.01
        d = Gradient(a,b,f)
