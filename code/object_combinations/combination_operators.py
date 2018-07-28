#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
returns various alternative combinations between A and B
"""
__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

"""
original GLSL implementation by MERCURY http://mercury.sexy/hg_sdf
Java port by W:Blut (Frederik Vanhoutte): https://github.com/wblut/HE_Mesh/blob/master/src/math/wblut/math/WB_SDF.java
"""

"""
original copyright note:

////////////////////////////////////////////////////////////////
//
//                           HG_SDF
//
//     GLSL LIBRARY FOR BUILDING SIGNED DISTANCE BOUNDS
//
//     version 2016-01-10
//
//     Check http://mercury.sexy/hg_sdf for updates
//     and usage examples. Send feedback to spheretracing@mercury.sexy.
//
//     Brought to you by MERCURY http://mercury.sexy
//
//
//
// Released as Creative Commons Attribution-NonCommercial (CC BY-NC)
//
////////////////////////////////////////////////////////////////
//
// How to use this:
//
// 1. Build some system to #include glsl files in each other.
//   Include this one at the very start. Or just paste everywhere.
// 2. Build a sphere tracer. See those papers:
//   * "Sphere Tracing" http://graphics.cs.illinois.edu/sites/default/files/zeno.pdf
//   * "Enhanced Sphere Tracing" http://lgdv.cs.fau.de/get/2234
//   The Raymnarching Toolbox Thread on pouet can be helpful as well
//   http://www.pouet.net/topic.php?which=7931&page=1
//   and contains links to many more resources.
// 3. Use the tools in this library to build your distance bound f().
// 4. ???
// 5. Win a compo.
//
// (6. Buy us a beer or a good vodka or something, if you like.)
//
////////////////////////////////////////////////////////////////
//
// Table of Contents:
//
// * Helper functions and macros
// * Collection of some primitive objects
// * Domain Manipulation operators
// * Object combination operators
//
////////////////////////////////////////////////////////////////
//
// Why use this?
//
// The point of this lib is that everything is structured according
// to patterns that we ended up using when building geometry.
// It makes it more easy to write code that is reusable and that somebody
// else can actually understand. Especially code on Shadertoy (which seems
// to be what everybody else is looking at for "inspiration") tends to be
// really ugly. So we were forced to do something about the situation and
// release this lib ;)
//
// Everything in here can probably be done in some better way.
// Please experiment. We'd love some feedback, especially if you
// use it in a scene production.
//
// The main patterns for building geometry this way are:
// * Stay Lipschitz continuous. That means: don't have any distance
//   gradient larger than 1. Try to be as close to 1 as possible -
//   Distances are euclidean distances, don't fudge around.
//   Underestimating distances will happen. That's why calling
//   it a "distance bound" is more correct. Don't ever multiply
//   distances by some value to "fix" a Lipschitz continuity
//   violation. The invariant is: each fSomething() function returns
//   a correct distance bound.
// * Use very few primitives and combine them as building blocks
//   using combine opertors that preserve the invariant.
// * Multiply objects by repeating the domain (space).
//   If you are using a loop inside your distance function, you are
//   probably doing it wrong (or you are building boring fractals).
// * At right-angle intersections between objects, build a new local
//   coordinate system from the two distances to combine them in
//   interesting ways.
// * As usual, there are always times when it is best to not follow
//   specific patterns.
//
////////////////////////////////////////////////////////////////
//
// FAQ
//
// Q: Why is there no sphere tracing code in this lib?
// A: Because our system is way too complex and always changing.
//    This is the constant part. Also we'd like everyone to
//    explore for themselves.
//
// Q: This does not work when I paste it into Shadertoy!!!!
// A: Yes. It is GLSL, not GLSL ES. We like real OpenGL
//    because it has way more features and is more likely
//    to work compared to browser-based WebGL. We recommend
//    you consider using OpenGL for your productions. Most
//    of this can be ported easily though.
//
// Q: How do I material?
// A: We recommend something like this:
//    Write a material ID, the distance and the local coordinate
//    p into some global variables whenever an object's distance is
//    smaller than the stored distance. Then, at the end, evaluate
//    the material to get color, roughness, etc., and do the shading.
//
// Q: I found an error. Or I made some function that would fit in
//    in this lib. Or I have some suggestion.
// A: Awesome! Drop us a mail at spheretracing@mercury.sexy.
//
// Q: Why is this not on github?
// A: Because we were too lazy. If we get bugged about it enough,
//    we'll do it.
//
// Q: Your license sucks for me.
// A: Oh. What should we change it to?
//
// Q: I have trouble understanding what is going on with my distances.
// A: Some visualization of the distance field helps. Try drawing a
//    plane that you can sweep through your scene with some color
//    representation of the distance field at each point and/or iso
//    lines at regular intervals. Visualizing the length of the
//    gradient (or better: how much it deviates from being equal to 1)
//    is immensely helpful for understanding which parts of the
//    distance field are broken.
//
////////////////////////////////////////////////////////////////

"""

import rhinoscriptsyntax as rs
import math
import Rhino.Geometry as rg

"""
////////////////////////////////////////////////////////////////
//
//             OBJECT COMBINATION OPERATORS
//
////////////////////////////////////////////////////////////////
//
// We usually need the following boolean operators to combine two objects:
// Union: OR(a,b)
// Intersection: AND(a,b)
// Difference: AND(a,!b)
// (a and b being the distances to the objects).
//
// The trivial implementations are min(a,b) for union, max(a,b) for intersection
// and max(a,-b) for difference. To combine objects in more interesting ways to
// produce rounded edges, chamfers, stairs, etc. instead of plain sharp edges we
// can use combination operators. It is common to use some kind of "smooth minimum"
// instead of min(), but we don't like that because it does not preserve Lipschitz
// continuity in many cases.
//
// Naming convention: since they return a distance, they are called fOpSomething.
// The different flavours usually implement all the boolean operators above
// and are called fOpUnionRound, fOpIntersectionRound, etc.
//
// The basic idea: Assume the object surfaces intersect at a right angle. The two
// distances <a> and <b> constitute a new local two-dimensional coordinate system
// with the actual intersection as the origin. In this coordinate system, we can
// evaluate any 2D distance function we want in order to shape the edge.
//
// The operators below are just those that we found useful or interesting and should
// be seen as examples. There are infinitely more possible operators.
//
// They are designed to actually produce correct distances or distance bounds, unlike
// popular "smooth minimum" operators, on the condition that the gradients of the two
// SDFs are at right angles. When they are off by more than 30 degrees or so, the
// Lipschitz condition will no longer hold (i.e. you might get artifacts). The worst
// case is parallel surfaces that are close to each other.
//
// Most have a float argument <r> to specify the radius of the feature they represent.
// This should be much smaller than the object size.
//
// Some of them have checks like "if ((-a < r) && (-b < r))" that restrict
// their influence (and computation cost) to a certain area. You might
// want to lift that restriction or enforce it. We have left it as comments
// in some cases.
//
// usage example:
//
// float fTwoBoxes(vec3 p) {
//   float box0 = fBox(p, vec3(1));
//   float box1 = fBox(p-vec3(1), vec3(1));
//   return fOpUnionChamfer(box0, box1, 0.2);
// }
//
////////////////////////////////////////////////////////////////

"""
def get_groove(a,b):
    return max(a, min(a + ra, rb - abs(b)))

def get_addition_chamfer(a,b):
    return min(min(a, b), (a - ra + b) * math.sqrt(0.5))

def get_intersection_chamfer(a,b):
    return max(max(a, b), (a + ra + b) * math.sqrt(0.5))

def get_subtraction_chamfer(a,b):
    return get_intersection_chamfer(a,-b)

def get_addition_stairs(a,b):
    s = ra / n;
    u = b - ra;
    return min(min(a, b), 0.5 * (u + a + abs((u - a + s) % (2 * s) - s)))

def get_intersection_stairs(a,b):
    return -get_addition_stairs(-a,-b)

def get_subtraction_stairs(a,b):
    return -get_addition_stairs(-a,b)

def get_tongue(a,b):
    return min(a, max(a - ra, abs(b) - rb))
def get_v_engrave(a,b):
    return max(a, (a + ra - abs(b)) * math.sqrt(0.5))
def get_pipe(a,b):
    l = math.sqrt(a*a+b*b)
    return l - ra

def get_addition_round(a,b):
    v1 = rg.Vector2d(ra-a,ra-b)
    v2 = rg.Vector2d(0,0)
    u = max2D(v1,v2)
    return max(ra, min(a, b)) - u.Length

def get_intersection_round(a,b):
    u = max2D(rg.Vector2d(ra + a, ra + b), rg.Vector2d(0, 0))
    return min(-ra, max(a, b)) + u.Length

def get_subtraction_round(a,b):
    return get_intersect_round(a,-b)

def get_addition_columns(a,b):
    sq2 = math.sqrt(2.0)
    if a<ra and b<ra:
        p = rg.Vector2d(a,b)
        columnradius = ra * sq2 / ((n-1) * 2 + sq2)
        p = rot45(p)
        p = rs.VectorSubtract(p,rg.Vector3d(sq2 / 2 * ra,0,0))
        p = rs.VectorAdd(p,rg.Vector3d(columnradius*sq2,columnradius*sq2,0))
        if n%2==1:
            p = rs.VectorAdd(p,rg.Vector3d(0,columnradius,0))
        p.Y = mod1(p.Y, columnradius*2)
        result = p.Length-columnradius
        result = min(result, p.X)
        result = min(result, a)
        return min(result, b)
    else:
        return min(a,b)

def get_subtraction_columns(a,b):
    sq2 = math.sqrt(2.0)
    a = -a
    m = min(a,b)
    if a<ra and b<ra:
        p = rg.Vector2d(a,b)
        columnradius = ra * sq2 / ((n-1) * 2 + sq2)
        p = rot45(p)
        p = rs.VectorAdd(p,rg.Vector3d(0,columnradius,0))
        p = rs.VectorSubtract(p,rg.Vector3d(sq2 / 2 * ra,sq2 / 2 * ra, 0))
        p = rs.VectorAdd(p,rg.Vector3d(-columnradius*sq2/2,-columnradius*sq2/2,0))
        if n%2==1:
            p = rs.VectorAdd(p,rg.Vector3d(0,columnradius,0))
        p.Y = mod1(p.Y, columnradius*2)
        result = -p.Length+columnradius
        result = max(result,p.X)
        result = min(result,a)
        return -min(result,b)
    else:
        return -m

def get_intersection_columns(a,b):
    return get_subtraction_columns(a,-b)

"""
HELPER FUNCTIONS
"""
def rot45(v):
    f = math.sqrt(0.5)
    vo = rg.Vector3d((v.X+v.Y)*f, (v.Y-v.X)*f,0)
    return vo

def mod1(p,size):
    halfsize = size * 0.5
    p = (p + halfsize) % size - halfsize
    return p

def max2D(v,w):
    return rg.Vector2d(max(v.X, w.X), max(v.Y, w.Y))

# input check
if not ra:
    ra = 2.0
if not rb:
    rb = ra
if not n:
    n = 3
if not mode:
    mode = 0
if mode > 15:
    mode = 0

# switch mode
vals = [9999.9 for _ in A]
if mode==0:
    vals = [get_addition_chamfer(u,v) for u,v in zip(A,B)]
elif mode==1:
    vals = [get_intersection_chamfer(u,v) for u,v in zip(A,B)]
elif mode==2:
    vals = [get_subtraction_chamfer(u,v) for u,v in zip(A,B)]
elif mode==3:
    vals = [get_addition_round(u,v) for u,v in zip(A,B)]
elif mode==4:
    vals = [get_intersection_round(u,v) for u,v in zip(A,B)]
elif mode==5:
    vals = [get_subtraction_round(u,v) for u,v in zip(A,B)]
elif mode==6:
    vals = [get_addition_columns(u,v) for u,v in zip(A,B)]
elif mode==7:
    vals = [get_intersection_columns(u,v) for u,v in zip(A,B)]
elif mode==8:
    vals = [get_subtraction_columns(u,v) for u,v in zip(A,B)]
elif mode==9:
    vals = [get_addition_stairs(u,v) for u,v in zip(A,B)]
elif mode==10:
    vals = [get_intersection_stairs(u,v) for u,v in zip(A,B)]
elif mode==11:
    vals = [get_subtraction_stairs(u,v) for u,v in zip(A,B)]
elif mode==12:
    vals = [get_groove(u,v) for u,v in zip(A,B)]
elif mode==13:
    vals = [get_tongue(u,v) for u,v in zip(A,B)]
elif mode==14:
    vals = [get_v_engrave(u,v) for u,v in zip(A,B)]
elif mode==15:
    vals = [get_pipe(u,v) for u,v in zip(A,B)]

# return list
a = vals
