"""Creates a Boolean union.
    Inputs:
        a: list of / single sdf object(s)
        b: second sdf object
    Output:
        d: the union object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Union(object):
    """
    boolean union of two or more objects
    """
    def __init__(self, obja=None, objb=None):
        if type(obja)==type([]):
            self.objs = obja
        else:
            self.objs = [obja,objb]

    def get_distance(self,x,y,z):
        ds = [o.get_distance(x,y,z) for o in self.objs]
        return min(ds)

if __name__=="__main__":
    if a is not None:
        d = Union(a,b)
