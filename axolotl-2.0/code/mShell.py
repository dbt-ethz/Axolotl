"""Creates a shell from a solid.
    Inputs:
        x: the solid sdf object
        t: thickness of the shell
        s: side factor (1: inside, 0.5: half/half, 0: outside)
    Output:
        d: the shell object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs

class Shell(object):
    """
    creates a shell of thickness d
    side factor s:
        1.0 > inside
        0.5 > half half
        0.0 > outside
    """

    def __init__(self, obj, d=1.0, s=0.0):
        self.o = obj
        self.d = d
        self.s = s

    def get_distance(self,x,y,z):
        do = self.o.get_distance(x,y,z)
        return abs(do + (self.s-0.5)*self.d)-self.d/2.0

if __name__=="__main__":
    if x is not None:
        if t is None:
            t = 1.0
        if s is None:
            s = 0.5
        d = Shell(x,t,s)
