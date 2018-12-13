"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "user"
__version__ = "2018.12.11"

import math

class TPMS(object):
    def __init__(self, w=10.0):
        self.wl = w
        self.fact = self.wl/(math.pi)

    def get_distance(self,x,y,z):
        px = x/self.fact
        py = y/self.fact
        pz = z/self.fact
        return self.get_value(px,py,pz)

    def get_value(self,x,y,z):
        return 0

class Gyroid(TPMS):
    def get_value(self,px,py,pz):
        return math.sin(px)*math.cos(py) + math.sin(py)*math.cos(pz) + math.sin(pz)*math.cos(px)

class SchwartzP(TPMS):
    def get_value(self,px,py,pz):
        return math.cos(px)+math.cos(py)+math.cos(pz)

class Diamond(TPMS):
    def get_value(self,px,py,pz):
        return (
            math.sin(px) * math.sin(py) * math.sin(pz) +
            math.sin(px) * math.cos(py) * math.cos(pz) +
            math.cos(px) * math.sin(py) * math.cos(pz) +
            math.cos(px) * math.cos(py) * math.sin(pz))

class FischerKoch(TPMS):
    def get_value(self,px,py,pz):
        return (
            math.cos(2*px) * math.sin(py) * math.cos(pz) +
            math.cos(2*py) * math.sin(pz) * math.cos(px) +
            math.cos(2*pz) * math.sin(px) * math.cos(py))

if __name__=="__main__":
    if i is None:
        i = 0
    if w is None:
        w = 10.0
    tpms = [Gyroid(w),SchwartzP(w),Diamond(w),FischerKoch(w)]
    d = tpms[i]
    
