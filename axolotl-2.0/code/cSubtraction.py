"""Creates a Boolean subtraction a-b.
    Inputs:
        a: sdf object to subtract from
        b: sdf object to subtract
    Output:
        d: the subtraction/difference object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Subtraction(object):
    """
    boolean subtraction of a minus b
    """
    def __init__(self, obja, objb):
        self.a = obja
        self.b = objb

    def get_distance(self,x,y,z):
        da = self.a.get_distance(x,y,z)
        db = self.b.get_distance(x,y,z)
        return max(da,-db)

if __name__=="__main__":
    if a is not None and b is not None:
        d = Subtraction(a,b)
        print d.get_distance(3,4,5)
