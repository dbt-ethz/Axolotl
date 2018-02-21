# Examples

## General Info
Every **AXOLOTL** definition consists of _three_ main parts:

1. The discretisation of space into a three dimensional _grid of voxels_. This can either be done from a simple box or from a grayscale raster image describing the topography of a landscape. The outputs of this part are
 * the resolution in X, Y and Z (required by other components, e.g. blur and Millipede isosurface) and
 * a one dimensional list of query points for the distance calculations (`pts`)
1. Building up the _CSG (constructive solid geometry) tree_. All the components that create geometry take as an input - beside their own geometric properties like center and radius for a sphere - the list of points from step one (`pts`) and outputs a one dimensional list of distances `a` as floats. Two of these lists can be combined by  Boolean operation components `Union`, `Subtraction`, `Intersection` and `Blending`. They take as input two `a` lists and output the result as another `a` list that can be fed into other Boolean operations again.
1. The _visualisation_ part, where the voxel field of distance values is turned into either geometry (using Millipede's isosurface component) or displayed as a volume of dots whose colour corresponds to its distance value.

## 00 Basic
![basic](00_basic.png)

## 01 ...
more to follow
