"""Creates a sparse voxel octree (SVO) subdivision.
    Inputs:
        x: the sdf object used for distance calculation
        p: the center point of the root node (default: 0,0,0)
        d: the edge length of the root node (default: 6.0)
        n: the maximum number of subdivisions (default: 4)
    Output:
        t: the octree object, t.leafs is a list of leaf nodes (for MC meshing)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
from math import sqrt

class OcTree(object):
    """
    sparse voxel octree (SVO) class for adaptive subdivision
    """
    def __init__(self, pt, ws):
        self.worldsize = float(ws)
        self.maxlevels = 3
        #self.sqrt2 = sqrt(2.0)
        self.sqrt3 = sqrt(3.0)
        self.pos = pt
        self.rootnode = OctNode(pt.X,pt.Y,pt.Z, ws, 0)
        self.distobj = None
        self.leafs = []

    def set_level(self, n):
        self.maxlevels = int(n)

    def divide(self, node):
        d = self.distobj.get_distance(node.pos.X, node.pos.Y, node.pos.Z)
        node.distance = d

        if node.level < self.maxlevels:
            if abs(d) < self.sqrt3 * node.edge/2.0:
                node.divide_node()
                for b in node.branches:
                    self.divide(b)
        else:
            self.leafs.append(node)

class OctNode(object):
    """
    node of octree that is either leaf node
    or has 8 child nodes as branches
    """
    def __init__(self, x,y,z, s, l):
        self.pos = rg.Vector3f(x,y,z)
        self.edge = s
        self.level = l
        self.branches = None
        self.distance = 0.0

    def divide_node(self):
        self.branches = []
        qs = self.edge/4.0
        nl = self.level + 1
        self.branches.append(OctNode(self.pos.X-qs, self.pos.Y-qs, self.pos.Z-qs, qs*2, nl))
        self.branches.append(OctNode(self.pos.X+qs, self.pos.Y-qs, self.pos.Z-qs, qs*2, nl))
        self.branches.append(OctNode(self.pos.X-qs, self.pos.Y+qs, self.pos.Z-qs, qs*2, nl))
        self.branches.append(OctNode(self.pos.X+qs, self.pos.Y+qs, self.pos.Z-qs, qs*2, nl))
        self.branches.append(OctNode(self.pos.X-qs, self.pos.Y-qs, self.pos.Z+qs, qs*2, nl))
        self.branches.append(OctNode(self.pos.X+qs, self.pos.Y-qs, self.pos.Z+qs, qs*2, nl))
        self.branches.append(OctNode(self.pos.X-qs, self.pos.Y+qs, self.pos.Z+qs, qs*2, nl))
        self.branches.append(OctNode(self.pos.X+qs, self.pos.Y+qs, self.pos.Z+qs, qs*2, nl))

if __name__=="__main__":
    if x is not None:
        if p is None:
            p = rg.Point3f(0,0,0)
        if d is None:
            d = 6.0
        if n is None:
            n = 4
        t = OcTree(p,d)
        t.distobj = x
        t.set_level(n)
        t.divide(t.rootnode)
