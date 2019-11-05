"""Creates a voronoi tessellation of space.
    Inputs:
        p: list of cell center points
        l: list of cell center lines
        t: thickness of the cell walls
        c: boolean toggle, True: closed surfaces between cells, False: edge truss only
    Output:
        d: the voronoi object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
from math import sqrt

class Voronoi(object):
    def __init__(self, points=None, lines=None, thickness=1.0):
        self.points = points
        self.lines = lines
        print(len(self.lines))
        self.thickness = thickness

    def get_distance(self, x, y, z):
        querypoint = rg.Point3d(x,y,z)
        distances = []

        # points
        if self.points is not None:
            pd = [p.DistanceTo(querypoint) for p in self.points]
            distances.extend(pd)

        # lines
        if self.lines is not None:
            ld = [segment_distance(l, querypoint) for l in self.lines]
            distances.extend(ld)

        distances.sort()
        if c:
            return abs(distances[0]-distances[1]) - self.thickness
        else:
            s = sum([abs(distances[i]-distances[(i+1)%3]) for i in range(2)])
            return s - self.thickness

def segment_distance(line, point):
    x1,y1,z1 = line.From
    x2,y2,z2 = line.To
    x3,y3,z3 = point

    px = x2-x1
    py = y2-y1
    pz = z2-z1

    norm = px*px + py*py + pz*pz

    u = ((x3 - x1) * px + (y3 - y1) * py + (z3 - z1) * pz) / float(norm)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py
    z = z1 + u * pz

    dx = x - x3
    dy = y - y3
    dz = z - z3

    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance

    dist = sqrt(dx*dx + dy*dy + dz*dz)

    return dist


if __name__=='__main__':
    d = Voronoi(points=p, lines=l, thickness=t)
