"""Volumentric Perlin Noise.
    Inputs:
        w: the wavelength (default = 16)
        a: the amplitude (default = 4)
    Output:
        d: distance object (sdf)"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = ['<bernhard@arch.ethz.ch>']

#Source: https://rosettacode.org/wiki/Perlin_noise#Python

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

class PerlinNoise(object):
    def __init__(self,w=10.0, a=10.0):
        self.w = w
        self.a = a
        self.p = self.setup_p()

    def get_distance(self, x, y, z):
        x = abs(x)/self.w
        y = abs(y)/self.w
        z = abs(z)/self.w
        X = int(x) & 255                  # FIND UNIT CUBE THAT
        Y = int(y) & 255                  # CONTAINS POINT.
        Z = int(z) & 255
        x -= int(x)                                # FIND RELATIVE X,Y,Z
        y -= int(y)                                # OF POINT IN CUBE.
        z -= int(z)
        u = self.fade(x)                                # COMPUTE FADE CURVES
        v = self.fade(y)                                # FOR EACH OF X,Y,Z.
        w = self.fade(z)
        A = self.p[X  ]+Y; AA = self.p[A]+Z; AB = self.p[A+1]+Z      # HASH COORDINATES OF
        B = self.p[X+1]+Y; BA = self.p[B]+Z; BB = self.p[B+1]+Z      # THE 8 CUBE CORNERS,

        v = self.lerp(w, self.lerp(v, self.lerp(u, self.grad(self.p[AA  ], x  , y  , z   ),  # AND ADD
                                        self.grad(self.p[BA  ], x-1, y  , z   )), # BLENDED
                                        self.lerp(u, self.grad(self.p[AB  ], x  , y-1, z   ),  # RESULTS
                                        self.grad(self.p[BB  ], x-1, y-1, z   ))),# FROM  8
                                        self.lerp(v, self.lerp(u, self.grad(self.p[AA+1], x  , y  , z-1 ),  # CORNERS
                                        self.grad(self.p[BA+1], x-1, y  , z-1 )), # OF CUBE
                                        self.lerp(u, self.grad(self.p[AB+1], x  , y-1, z-1 ),
                                        self.grad(self.p[BB+1], x-1, y-1, z-1 ))))
        return v * self.a

    def fade(self, t):
        return t ** 3 * (t * (t * 6 - 15) + 10)

    def lerp(self, t, a, b):
        return a + t * (b - a)

    def grad(self, hash, x, y, z):
        h = hash & 15                      # CONVERT LO 4 BITS OF HASH CODE
        u = x if h<8 else y                # INTO 12 GRADIENT DIRECTIONS.
        v = y if h<4 else (x if h in (12, 14) else z)
        return (u if (h&1) == 0 else -u) + (v if (h&2) == 0 else -v)

    def setup_p(self):
        p = [None] * 512
        permutation = [151,160,137,91,90,15,
           131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,
           190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
           88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
           77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
           102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
           135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
           5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
           223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
           129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
           251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
           49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
           138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
        for i in range(256):
            p[256+i] = p[i] = permutation[i]
        return p

if __name__=="__main__":
    if w is None:
        w = 10.0
    if a is None:
        a = 10.0
    d = PerlinNoise(w,a)
    print d.get_distance(2.3,3.4,5.6)
    
