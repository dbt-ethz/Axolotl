"""
Calculates the shortest path between to grid locations in a voxel space.

    Inputs:
        omap: list of obstacles, 1 is free, 0 is occupied
        sp: the starting point
        tp: the target point
        nx: number of cells in x direction
        ny: number of cells in y direction
        nz: number of cells in z direction
        box: the bounding box of the voxel space
        c: type of neighborhood, allowed moves.
            1 >  6 neighbors sharing a face
            2 > 18 neighbors sharing an edge
            3 > 26 neighbors sharing a vertex
    Output:
        dsts: list of distance values for each cell to the target.
        route: a list of tuples along the path, format: (distance, ix, iy, iz)
"""

# blogpost here: https://realitybytes.blog/2017/07/11/graph-based-path-planning-dijkstras-algorithm/
# adapted from here: https://github.com/atomoclast/realitybytes_blogposts/blob/master/pathplanning/dijkstra.py

import math

if not c:
    c==3
if c<1:
    c==1
if c>3:
    c==3

# precalculate distances
dists = [1, math.sqrt(2), math.sqrt(3)]

# create a list of directions with x,y and z offsets
directions = []

for i in range(-1,2):
    for j in range(-1,2):
        for k in range(-1,2):
            l = [i,j,k]
            s = sum([abs(v) for v in l])
            if s>0 and s<=c:
                l.append(s-1)
                directions.append(l)

def dijkstra(occ_map, start, goal):
    """
    occ_map: list (of lists (of lists)) of possible moves, 1 = free, possible, 0 = occupied
    start, goal: tuple of (column,row,layer) indices (x,y,z) coordinates
    """
    goal_found = False

    possible_nodes = [[[0 for x in range(nx)] for y in range(ny)] for z in range(nz)]
    dist_map =      [[[-1 for x in range(nx)] for y in range(ny)] for z in range(nz)]

    current_x, current_y, current_z = start
    possible_nodes[current_z][current_y][current_x] = 5 # somewhat arbitrary number, good for plotting with matplotlib
    dist_map[current_z][current_y][current_x] = 0

    g_value = 0
    frontier_nodes = [(g_value, current_x, current_y, current_z)] # dist, x, y, z
    searched_nodes = []
    parent_node = {}  # Dictionary that Maps {child node : parent node}

    while len(frontier_nodes) != 0:
        frontier_nodes.sort(reverse=True) #sort from shortest distance to farthest
        current_node = frontier_nodes.pop()
        if current_node[1] == goal[0] and current_node[2] == goal[1] and current_node[3] == goal[2]:
            # print "Goal found!"
            goal_found = True
            break
        g_value, current_x, current_y, current_z = current_node
        dist_map[current_z][current_y][current_x] = g_value

        for di in directions:
            possible_expansion_x = current_x + di[0]
            possible_expansion_y = current_y + di[1]
            possible_expansion_z = current_z + di[2]

            if 0<=possible_expansion_x<nx and 0<=possible_expansion_y<ny and 0<=possible_expansion_z<nz:
                try:
                    unsearched_node = possible_nodes[possible_expansion_z][possible_expansion_y][possible_expansion_x] == 0
                    open_node = occ_map[possible_expansion_z][possible_expansion_y][possible_expansion_x] == 1
                except:
                    unsearched_node = False
                    open_node = False
                if unsearched_node and open_node:
                    possible_nodes[possible_expansion_z][possible_expansion_y][possible_expansion_x] = 3
                    cost = dists[di[3]]
                    possible_node = (g_value + cost, possible_expansion_x, possible_expansion_y, possible_expansion_z)
                    frontier_nodes.append(possible_node)
                    parent_node[possible_node] = current_node

    if goal_found:
        # print "Generating path..."
        route = []
        route.append((g_value,goal[0],goal[1],goal[2]))
        child_node = current_node
        while parent_node.has_key(child_node):
            route.append(parent_node[child_node])
            child_node = parent_node[child_node]
            route.sort()
        route.reverse()

        return flatten(dist_map), route

    else:
        print "goal not found"
        return flatten(dist_map), None

def flatten(arr3d):
    arr1D = []
    for x in range(len(arr3d[0][0])):
       for y in range(len(arr3d[0])):
            for z in range(len(arr3d)):
                arr1D.append(arr3d[z][y][x])
    return arr1D

def fold(arr1d):
    arr3d = [[[0 for x in range(nx)] for y in range(ny)] for z in range(nz)]
    i = 0
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                arr3d[z][y][x] = omap[i]
                i+=1
    return arr3d

if __name__=='__main__':
    dx = box.X[1] - box.X[0]
    dy = box.Y[1] - box.Y[0]
    dz = box.Z[1] - box.Z[0]
    dix = dx/(nx-1)
    diy = dy/(ny-1)
    diz = dz/(nz-1)
    sx = int(round((sp.X-box.X[0])/dix))
    sy = int(round((sp.Y-box.Y[0])/diy))
    sz = int(round((sp.Z-box.Z[0])/diz))
    tx = int(round((tp.X-box.X[0])/dix))
    ty = int(round((tp.Y-box.Y[0])/diy))
    tz = int(round((tp.Z-box.Z[0])/diz))

    print sx,sy,sz,tx,ty,tz

    occ_map = fold(omap)
    dsts,route = dijkstra(occ_map,(sx,sy,sz),(tx,ty,tz))
