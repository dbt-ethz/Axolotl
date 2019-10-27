using System;
using System.Collections;
using System.Collections.Generic;

using Rhino;
using Rhino.Geometry;

using Grasshopper;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;
using Grasshopper.Kernel.Types;

using System.IO;
using System.Linq;
using System.Data;
using System.Drawing;
using System.Reflection;
using System.Windows.Forms;
using System.Xml;
using System.Xml.Linq;
using System.Runtime.InteropServices;

using Rhino.DocObjects;
using Rhino.Collections;
using GH_IO;
using GH_IO.Serialization;

/// <summary>
/// This class will be instantiated on demand by the Script component.
/// </summary>
public class Script_Instance : GH_ScriptInstance
{
#region Utility functions
  /// <summary>Print a String to the [Out] Parameter of the Script component.</summary>
  /// <param name="text">String to print.</param>
  private void Print(string text) { /* Implementation hidden. */ }
  /// <summary>Print a formatted String to the [Out] Parameter of the Script component.</summary>
  /// <param name="format">String format.</param>
  /// <param name="args">Formatting parameters.</param>
  private void Print(string format, params object[] args) { /* Implementation hidden. */ }
  /// <summary>Print useful information about an object instance to the [Out] Parameter of the Script component. </summary>
  /// <param name="obj">Object instance to parse.</param>
  private void Reflect(object obj) { /* Implementation hidden. */ }
  /// <summary>Print the signatures of all the overloads of a specific method to the [Out] Parameter of the Script component. </summary>
  /// <param name="obj">Object instance to parse.</param>
  private void Reflect(object obj, string method_name) { /* Implementation hidden. */ }
#endregion

#region Members
  /// <summary>Gets the current Rhino document.</summary>
  private readonly RhinoDoc RhinoDocument;
  /// <summary>Gets the Grasshopper document that owns this script.</summary>
  private readonly GH_Document GrasshopperDocument;
  /// <summary>Gets the Grasshopper script component that owns this script.</summary>
  private readonly IGH_Component Component;
  /// <summary>
  /// Gets the current iteration count. The first call to RunScript() is associated with Iteration==0.
  /// Any subsequent call within the same solution will increment the Iteration count.
  /// </summary>
  private readonly int Iteration;
#endregion

  /// <summary>
  /// This procedure contains the user code. Input parameters are provided as regular arguments,
  /// Output parameters as ref arguments. You don't have to assign output parameters,
  /// they will have a default value.
  /// </summary>
  private void RunScript(Box Box, double dim, ref object nx, ref object ny, ref object nz, ref object pts)
  {
    double dx = Box.X[1] - Box.X[0];
    double dy = Box.Y[1] - Box.Y[0];
    double dz = Box.Z[1] - Box.Z[0];

    int nxt = (int) Math.Round(dx / dim) + 1;
    int nyt = (int) Math.Round(dy / dim) + 1;
    int nzt = (int) Math.Round(dz / dim) + 1;

    double dimx = dx / (nxt - 1);
    double dimy = dy / (nyt - 1);
    double dimz = dz / (nzt - 1);

    nx = nxt;
    ny = nyt;
    nz = nzt;

    Point3d[] res = new Point3d[nxt * nyt * nzt];
    int i = 0;
    for (int x = 0; x < nxt; x++) {
      for (int y = 0; y < nyt; y++) {
        for (int z = 0; z < nzt; z++) {
          double px = Box.Center[0] - dx / 2 + x * dimx;
          double py = Box.Center[1] - dy / 2 + y * dimy;
          double pz = Box.Center[2] - dz / 2 + z * dimz;
          res[i] = new Point3d(px, py, pz);
          i++;
        }
      }
    }
    pts = res;
  }

  // <Custom additional code>

  /// <summary>
  /// This method will be called once every solution, before any calls to RunScript.
  /// </summary>
  public override void BeforeRunScript()
  { }
  /// <summary>
  /// This method will be called once every solution, after any calls to RunScript.
  /// </summary>
  public override void AfterRunScript()
  { }

  // </Custom additional code>
}
