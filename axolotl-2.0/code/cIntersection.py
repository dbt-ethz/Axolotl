"""Creates a Boolean intersection.
    Inputs:
        a: list of / single sdf object(s)
        b: second sdf object
    Output:
        d: the intersection object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Intersection(object):
    """
    boolean intersection of two or more objects
    """
    def __init__(self, obja=None, objb=None):
        if type(obja)==type([]):
            self.objs = obja
        else:
            self.objs = [obja,objb]

    def get_distance(self,x,y,z):
        ds = [o.get_distance(x,y,z) for o in self.objs]
        return max(ds)

if __name__=="__main__":
    if len(a)>0:
        if len(a)==1:
            if b is not None:
                d = Intersection(a[0],b)
        else:
            d = Intersection(a)
