# Axolotl 2.0

* complete rework
* new icon set
* not (yet) backwards compatible
* not all components translated (yet)
* some new components not in 1.x

![Axolotl Logo](icons/palette.png)

## Primitives

| Icon | Name | Description | Inputs | Output(s) |
| --- | --- | --- | --- | --- |
| ![sphere](icons/sphere.png) | axSphere | Creates a shere | r: sphere radius | d: the sphere object (sdf) |
| ![box](icons/box.png) | axBox | Creates a box with an optional edge fillet. | a: length along the x axis <br> b: length along the y axis <br> c: length along the z axis <br> r: edge fillet radius | d: the box object (sdf) |
| ![cylinder](icons/cylinder.png) | axCylinder | Creates a cylinder. | r: radius of the cylinder <br> h: height of the cylinder | d: the cylinder object (sdf) |
| ![torus](icons/torus.png) | axTorus | Creates a torus. | r1: radius of the "donut" (axis) <br> r2: radius of the pipe | d: the torus object (sdf) |
| ![pipe](icons/pipe.png) | axPipe | Creates a pipe along a curve. | c: the axis curve <br> r1: radius at the start of the curve <br> r2: radius at the end of the curve | d: the pipe object (sdf) |
| ![plane](icons/plane.png) | axPlane | Creates a series of planes. | n: list of normal vectors <br> o: offset distance from the origin | d: the plane objects (sdf) |
