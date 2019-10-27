"""Creates a micro-structure / lattice using triply periodic minimal surfaces (TMPS).
    Inputs:
        i: index > 0: Gyroid / 1: SchwartzP / 2: Diamond / 3: FischerKoch
        w: the wavelength
    Output:
        d: the lattice object (sdf)
        n: list of TPMS names"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

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

class Lidinoid(TPMS):
    def get_value(self,px,py,pz):
        return (0.5 * (
            math.sin(2 * px) * math.cos(py) * math.sin(pz) +
            math.sin(2 * py) * math.cos(pz) * math.sin(py) +
            math.sin(2 * pz) * math.cos(px) * math.sin(py) ) -
            0.5 * (
            math.cos(2 * px) * math.cos(2 * py) +
            math.cos(2 * py) * math.cos(2 * pz) +
            math.cos(2 * pz) * math.cos(2 * px)) + 0.15)

class Neovius(TPMS):
    def get_value(self,px,py,pz):
        return (
	    3 * (math.cos(px) + math.cos(py) + math.cos(pz)) +
	    4 *  math.cos(px) * math.cos(py) * math.cos(pz))


if __name__=="__main__":
    if w is None:
        w = 10.0
    tpms = [Gyroid(w),SchwartzP(w),Diamond(w),FischerKoch(w),Lidinoid(w),Neovius(w)]
    if i is None:
        i = 0
    i = max(0,min(i,len(tpms)-1))
    d = tpms[i]
    n = ["Gyroid", "SchwartzP", "Diamond", "FischerKoch", "Lidinoid", "Neovius"]
