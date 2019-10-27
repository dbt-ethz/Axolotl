"""
gradient vectors from voxelspace
"""

__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

import rhinoscriptsyntax as rs
import math

def get_index(x,y,z):
    return x * nyz + y * nz + z

if __name__=="__main__":
    if not nx:
        nx = 0
    if not ny:
        ny = 0
    if not nz:
        nz = 0
    nyz = ny*nz
    nxy = nx*ny

    ukernel = [[1,2,1],[2,4,2],[1,2,1]]
    mkernel = [[0]*3]*3
    lkernel = [[-1,-2,-1],[-2,-4,-2],[-1,-2,-1]]
    kernel = [ukernel,mkernel,lkernel]

    #xval = [0 for _ in vals]
    #yval = [0 for _ in vals]
    #zval = [0 for _ in vals]
    nval = [0 for _ in vals]
    for x in range(1,nx-1):
        for y in range(1,ny-1):
            for z in range(1,nz-1):
                ix = get_index(x,y,z)
                vsx = 0
                vsy = 0
                vsz = 0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        for dz in range(-1,2):
                            it = get_index(x+dx,y+dy,z+dz)
                            vt = vals[it]
                            vsx += vt * kernel[dz+1][dx+1][dy+1]
                            vsy += vt * kernel[dy+1][dz+1][dx+1]
                            vsz += vt * kernel[dx+1][dy+1][dz+1]
                #xval[ix] = vsx
                #yval[ix] = vsy
                #zval[ix] = vsz
                nval[ix] = math.sqrt(vsx**2 + vsy**2 + vsz**2)
