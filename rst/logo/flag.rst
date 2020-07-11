Flag Geometry
#############

The U.s flag is well defined, so the **inkscape** processing of this component
was not needed. Instead, I looked at example SVG files that produce the flag,
and extracted code from those.

Here is the basic geometry from
http://https://www.chamberofcommerce.org/usflag/flagspecs.html:

..  image:: specflag.gif
    :align: center

The stars are positioned at the center of a circle of the defined radius. Each
point is located at an angle of 360/5 = 72 degrees, making the height of the
star a bit shorter than the width. Here is another image showing the positions
of the points that make up each star:

..  image:: star-points.gif
    :align: center

With these two figures, we can build a basic flag file using fairly simple SVG
commands.

