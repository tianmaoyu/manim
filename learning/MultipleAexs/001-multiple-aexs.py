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
class ThreeDRotation000(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)


        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))



        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))

        rad=-30*DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(ApplyMethod(axes1.apply_matrix, matrix_y))


        self.play(axes1.animate.shift([2,2,2]))

        self.move_camera(zoom=0.8,run_time=2)

        dot= Dot3D(point=[4,-4,1],depth_test=False)

        arrow1= OpenGLArrow3D(start=np.array([0,0,0]),end=[4,-4,1],depth_test=False)

        arrow2 = OpenGLArrow3D(start=np.array([2,2,2]), end=[4,-4,1],depth_test=False).set_color(YELLOW)

        self.play(Create(arrow1),Create(arrow2))
        self.play(Create(dot))

        labes=MathTex(r"P(4,-4,1)").scale(0.5)
        labes.shift([4,-4,1])
        self.add_fixed_orientation_mobjects(labes)

        arrow_t = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[2,2,2])
        self.play(Create(arrow_t))

        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(1)

        matrix = MathTex(r"""
        M
        =
        \begin{bmatrix}
        1 & 0& 0\\
        0 & 1& 0\\
        0 & 0& 1
        \end{bmatrix} """).scale(0.7)

        matrix2 = MathTex(r"""
        M =
        \begin{bmatrix} 
        cos(\alpha) & -sin(\alpha) &0 \\ 
        sin(\alpha) & cos(\alpha) &0\\
        0 & 0 &1
        \end{bmatrix} """).set_color(YELLOW).scale(0.7)

        self.add_fixed_in_frame_mobjects(matrix.to_corner(UL))

        self.add_fixed_in_frame_mobjects(matrix2.next_to(matrix,DOWN))

        self.wait(3)










with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    ThreeDRotation000().render()
    exit(1)
