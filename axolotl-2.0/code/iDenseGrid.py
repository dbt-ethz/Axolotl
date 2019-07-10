"""Samples a SDF object in a dense grid.
    Inputs:
        b: the bounding box
        d: the (approximate) spacing of the points
        o: the distance object
    Output:
        p: a list of points, xyz order
        v: a list of distance values corresponding to the points"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import math

class DenseGrid(object):
    def __init__(self, box=None, dim=1.0, o=None):
        self.box = box
        self.dx = box.X[1] - box.X[0]
        self.dy = box.Y[1] - box.Y[0]
        self.dz = box.Z[1] - box.Z[0]

        self.nx = int(round(self.dx/dim))+1
        self.ny = int(round(self.dy/dim))+1
        self.nz = int(round(self.dz/dim))+1

        self.dimx = self.dx/(self.nx-1)
        self.dimy = self.dy/(self.ny-1)
        self.dimz = self.dz/(self.nz-1)

        self.o = o

    def get_distances(self):
        p = []
        v = []
        for x in range(self.nx):
            for y in range(self.ny):
                for z in range(self.nz):
                    px = self.box.Center[0] - self.dx/2 + x*self.dimx
                    py = self.box.Center[1] - self.dy/2 + y*self.dimy
                    pz = self.box.Center[2] - self.dz/2 + z*self.dimz

                    p.append(rs.AddPoint(px,py,pz))
                    v.append(self.o.get_distance(px,py,pz))
        return p,v


if __name__=="__main__":
    if d is None:
        d = 1.0
    if b is not None and o is not None:
        dg = DenseGrid(box=b, dim=d, o=o)
        print(dg.dx, dg.dy, dg.dz)
        p, v = dg.get_distances()
