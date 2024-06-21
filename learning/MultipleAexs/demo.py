from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image


#
class MultipleAexs001(ThreeDScene):
    def construct(self):
        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        labels = axes1.get_axis_labels(x_label=MarkupText("北").scale(0.5), y_label=MarkupText("东").scale(0.5),
                                       z_label=MarkupText("地").scale(0.5))
        self.add(labels)
        label0 = labels[0]
        label0_1 = MarkupText("X")

        # label0.become(label0_1)
        self.wait()

        self.play(ReplacementTransform(label0_1, label0))


with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    MultipleAexs001().render()
    exit(1)