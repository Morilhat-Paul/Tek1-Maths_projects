<h1 align="center">
  <br>
  <br>
  <br>
  104-Intersection
  <br>
</h1>

&nbsp;

<h3 align="center">
    To create synthesis images (when doing ray tracing, for example), potential intersection points between light rays and scene objects<br>
    (here cylinders, spheres and cones) must be computed.<br>
    This is exactly what we had to do in this project.<br>
    <br>
    To do so, we needed to write a 3 dimensional equation of the considered surface,<br>
    and inject into it the equation of the straight line representing the light ray.<br>
    We’ll get a quadratic equation, with 0, 1, 2 or an infinite number of solutions that will give us the intersection points coordinates.<br>
    The straight line is defined by the coordinates of a point by which it passes through and the coordinates of a parallel vector.<br>
    O being the origin of the coordinate system, and X, Y and Z the axis.<br>
    <br>
    The surfaces that must be handled in this project are:
    <br>
    • O-centered spheres<br>
    • Cylinders of revolution around Z axis<br>
    • Cones of revolution around Z axis whose apex is O
</h3>

&nbsp;

## 🏅 Results

| Cat | Percentages |
|:--:|:--:|
| Rigor | 89.5% |
| Sphere | 100% |
| Cylinder | 77.8% |
| Cone | 80% |
| **Total** | **87%** |

&nbsp;

## ℹ️ Usage

```bash
./104intersection opt xp yp zp xv yv zv p
```

&nbsp;

## 📝 Description

```txt
opt -> surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone
(xp, yp, zp) -> coordinates of a point by which the light ray passes through
(xv, yv, zv) -> coordinates of a vector parallel to the light ray
p -> parameter: radius of the sphere, radius of the cylinder, or angle formed by the cone and the Z-axis
```
