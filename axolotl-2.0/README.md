# Axolotl 2.0

* complete rework
* new icon set
* not (yet) backwards compatible
* not all components translated (yet)
* some new components not in 1.x

![Axolotl Logo](icons/palette.png)

## Documentation
### Primitives

| Icon | Name | Description | Inputs | Output(s) |
| --- | --- | --- | --- | --- |
| ![sphere](icons/sphere.png) | axSphere | Creates a shere | r: sphere radius | d: the sphere object (sdf) |
| ![box](icons/box.png) | axBox | Creates a box with an optional edge fillet. | a: length along the x axis <br> b: length along the y axis <br> c: length along the z axis <br> r: edge fillet radius | d: the box object (sdf) |
| ![cylinder](icons/cylinder.png) | axCylinder | Creates a cylinder. | r: radius of the cylinder <br> h: height of the cylinder | d: the cylinder object (sdf) |
| ![torus](icons/torus.png) | axTorus | Creates a torus. | r1: radius of the "donut" (axis) <br> r2: radius of the pipe | d: the torus object (sdf) |
| ![pipe](icons/pipe.png) | axPipe | Creates a pipe along a curve. | c: the axis curve <br> r1: radius at the start of the curve <br> r2: radius at the end of the curve | d: the pipe object (sdf) |
| ![plane](icons/plane.png) | axPlane | Creates a series of planes. | n: list of normal vectors <br> o: offset distance from the origin | d: the plane objects (sdf) |

### Combinations

| Icon | Name | Description | Inputs | Output(s) |
| --- | --- | --- | --- | --- |
| ![union](icons/union.png) | axUnion | Creates a Boolean union. | a: list of / single sdf object(s) <br> b: second sdf object | d: the union object (sdf) |
| ![intersection](icons/intersection.png) | axIntersection | Creates a Boolean intersection. | a: list of / single sdf object(s) <br> b: second sdf object | d: the intersection object (sdf) |
| ![subtraction](icons/subtraction.png) | axSubtraction | Creates a Boolean subtraction `a-b`. | a: sdf object to subtract from <br> b: sdf object to subtract | d: the intersection object (sdf) |
| ![blend](icons/blend.png) | axBlend | Creates a smooth blend union. | a: first sdf object <br> b: second sdf object <br> f: smoothing factor (default 2.0) | d: the blend object (sdf) |
| ![morph](icons/morph.png) | axMorph | Morphs one object into another object. | a: first sdf object <br> b: second sdf object <br> f: morphing factor <br> f=0>d=a, f=1>d=b <br> `d=(1-f)*a+f*b` | d: the intermediate object (sdf) |

### Modifications

| Icon | Name | Description | Inputs | Output(s) |
| :--- | :--- | :--- | :--- | :--- |
| ![shell](icons/shell.png) | axShell | Creates a shell from a solid. | x: the solid sdf object <br> t: thickness of the shell <br> s: side factor (1: inside, 0.5: half/half, 0: outside) | d: the shell object (sdf) |
