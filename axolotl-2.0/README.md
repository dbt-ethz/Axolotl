# Axolotl 2.0

* complete rework
* new icon set
* not (yet) backwards compatible
* not all components translated (yet)
* some new components not in 1.x

![Axolotl Logo](icons/palette.png)

## Documentation
* [Primitives](#primitives)
* [Combinations](#combinations)
* [Modifications](#modifications)
* [Meshing](#meshing)

### Primitives

| Icon | Name | Description | Inputs | Output(s) |
| :--- | :--- | :--- | :--- | :--- |
| ![sphere](icons/sphere.png) | axSphere | Creates a shere | r: sphere radius | d: the sphere object (sdf) |
| ![box](icons/box.png) | axBox | Creates a box with an optional edge fillet. | a: length along the x axis <br> b: length along the y axis <br> c: length along the z axis <br> r: edge fillet radius | d: the box object (sdf) |
| ![cylinder](icons/cylinder.png) | axCylinder | Creates a cylinder. | r: radius of the cylinder <br> h: height of the cylinder | d: the cylinder object (sdf) |
| ![torus](icons/torus.png) | axTorus | Creates a torus. | r1: radius of the "donut" (axis) <br> r2: radius of the pipe | d: the torus object (sdf) |
| ![pipe](icons/pipe.png) | axPipe | Creates a pipe along a curve. | c: the axis curve <br> r1: radius at the start of the curve <br> r2: radius at the end of the curve | d: the pipe object (sdf) |
| ![plane](icons/plane.png) | axPlane | Creates a series of planes. | n: list of normal vectors <br> o: offset distance from the origin | d: the plane objects (sdf) |

### Combinations

| Icon | Name | Description | Inputs | Output(s) |
| :--- | :--- | :--- | :--- | :--- |
| ![union](icons/union.png) | axUnion | Creates a Boolean union. | a: list of / single sdf object(s) <br> b: second sdf object | d: the union object (sdf) |
| ![intersection](icons/intersection.png) | axIntersection | Creates a Boolean intersection. | a: list of / single sdf object(s) <br> b: second sdf object | d: the intersection object (sdf) |
| ![subtraction](icons/subtraction.png) | axSubtraction | Creates a Boolean subtraction `a-b`. | a: sdf object to subtract from <br> b: sdf object to subtract | d: the intersection object (sdf) |
| ![blend](icons/blend.png) | axBlend | Creates a smooth blend union. | a: first sdf object <br> b: second sdf object <br> f: smoothing factor (default 2.0) | d: the blend object (sdf) |
| ![morph](icons/morph.png) | axMorph | Morphs one object into another object. | a: first sdf object <br> b: second sdf object <br> f: morphing factor <br> f=0>d=a, f=1>d=b <br> `d=(1-f)*a+f*b` | d: the intermediate object (sdf) |

### Modifications

| Icon | Name | Description | Inputs | Output(s) |
| :--- | :--- | :--- | :--- | :--- |
| ![transform](icons/transform.png) | axTransform | Applies a matrix transformation to an object. | x: the sdf object to be transformed <br> m: the 4x4 transformation matrix (e.g. translation, rotation, shear...) | d: the transformed object (sdf) |
| ![shell](icons/shell.png) | axShell | Creates a shell from a solid. | x: the solid sdf object <br> t: thickness of the shell <br> s: side factor (1: inside, 0.5: half/half, 0: outside) | d: the shell object (sdf) |
| ![twist](icons/twist.png) | axTwist | Creates a twist object (works only for those who have a get_bounds method). | x: the solid sdf object to be twisted <br> a: the twist angle | d: the twist object (sdf) |
| ![gradient](icons/gradient.png) | axGradient | Creates a gradient by adding a fraction of object b to object a. | a: the base sdf object (modified) <br> b: the object to be added (modifier) <br> f: intensity factor <br> `d = a + f * b`, default: 0.01 | d: the modified object (sdf) |

### Meshing

| Icon | Name | Description | Inputs | Output(s) |
| :--- | :--- | :--- | :--- | :--- |
| ![octree](icons/octree.png) | axOctree | Creates a sparse voxel octree (SVO) subdivision. | x: the sdf object used for distance calculation <br> p: the center point of the root node (default: 0,0,0) <br> d: the edge length of the root node (default: 6.0) <br> n: the maximum number of subdivisions (default: 4) | t: the octree object, `t.leafs` is a list of leaf nodes (for MC meshing) |
| ![isosurface](icons/iso_mc.png) | axMarchingCubes | Creates a marching cubes isosurface. | t: the subdivided octree | m: the isosurface mesh <br> p: the leaf node center points (for debugging) |
