"""Creates a twist object (works only for those who have a get_bounds method).
    Inputs:
        x: the solid sdf object to be twisted
        a: the twist angle
    Output:
        d: the twist object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import math

class Twist(object):
    def __init__(self,obj=None, ang=0.0):
        self.o = obj
        self.angle = float(ang)

    def get_distance(self,x,y,z):
        bnds = self.o.get_bounds()
        t = (z-bnds[2])/(bnds[5]-bnds[2]) - 0.5
        theta = t*self.angle
        nx = (x*math.cos(theta) - y*math.sin(theta))
        ny = (x*math.sin(theta) + y*math.cos(theta))
        return self.o.get_distance(nx,ny,z)

if __name__=="__main__":
    if x is not None:
        if a is None:
            a = 1.0
        d = Twist(x,a)
