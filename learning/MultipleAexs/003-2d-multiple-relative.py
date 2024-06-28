from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_mobject import OpenGLGroup
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D, OpenGLArrow3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image


# 原点相同 只旋转
class Multiple2DRelative000(ThreeDScene):
    def construct(self):

        axes = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                    y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())

        dot = Dot(point=[2, 0.5, 0])
        lable = MarkupText("P(2,0.5)").scale(0.3)
        lable.next_to(dot, RIGHT, buff=0.1)
        self.add(lable)
        self.play(FadeIn(axes), FadeIn(dot), FadeIn(lable))

        self.wait()

        axes1 = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                     y_length=8, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        dot1 = Dot(point=[2, 0.5, 0], color=YELLOW)
        lable1 = MarkupText("P(2,0.5)").set_color(YELLOW).scale(0.3)
        lable1.next_to(dot1, RIGHT, buff=0.1)

        rad = 30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(
            ApplyMethod(axes1.apply_matrix, matrix_y),
            ApplyMethod(dot1.apply_matrix, matrix_y),
            ApplyMethod(lable1.apply_matrix, matrix_y)
        )

        self.play(
            axes.animate.set_opacity(0),
            lable.animate.set_opacity(0)
        )

        lable_XY = MarkupText("P(x,y)").set_color(YELLOW).scale(0.3)
        lable_XY.move_to(lable.get_center())
        self.add(lable_XY)

        self.wait()

        self.play(
            axes.animate.set_opacity(1),
            lable.animate.set_opacity(1),
            lable_XY.animate.set_opacity(0)
        )

        self.play(
            axes1.animate.set_opacity(0),
            lable1.animate.set_opacity(0)
        )

        lable1_XY= MarkupText("P(x,y)").set_color(YELLOW).scale(0.3)
        lable1_XY.move_to(lable1.get_center())
        lable1_XY.rotate(rad,about_point=ORIGIN)

        self.play(
            FadeIn(lable1_XY)
        )
        self.wait()


# 原点相同 只旋转-向量相等
class Multiple2DRelative001(ThreeDScene):
    def construct(self):

        axes = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                    y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())

        dot = Dot(point=[2, 0.5, 0])
        lable = MarkupText("P(2,0.5)").scale(0.3)
        lable.next_to(dot, RIGHT, buff=0.1)
        self.add(lable)
        self.play(FadeIn(axes), FadeIn(dot), FadeIn(lable))

        self.wait()

        axes1 = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                     y_length=8, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        dot1 = Dot(point=[2, 0.5, 0], color=YELLOW)
        lable1 = MarkupText("P(2,0.5)").set_color(YELLOW).scale(0.3)
        lable1.next_to(dot1, RIGHT, buff=0.1)

        rad = 30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(
            ApplyMethod(axes1.apply_matrix, matrix_y),
            ApplyMethod(dot1.apply_matrix, matrix_y),
            ApplyMethod(lable1.apply_matrix, matrix_y)
        )

        arrow= OpenGLArrow3D(start=ORIGIN,end=dot.get_center())


        self.play(
            axes.animate.set_opacity(0),
            lable.animate.set_opacity(0),
            FadeIn(arrow),
        )

        matrix = MathTex(r"""
               M_白=
               \begin{bmatrix}
               1 & 0& \\
               0 & 1& 
               \end{bmatrix} """,tex_template=TexTemplateLibrary.ctex)

        matrix2 = MathTex(r"""
               M_黄 =
               \begin{bmatrix} 
               cos(\theta) & -sin(\theta) \\ 
               sin(\theta) & cos(\theta) 
               \end{bmatrix} """,tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)

        self.play(
            Create(matrix.to_corner(UL)),
            Create(matrix2.next_to(matrix,direction=DOWN,aligned_edge=LEFT)),
        )

        self.wait()

        self.play(
            axes.animate.set_opacity(1),
            lable.animate.set_opacity(1),
            axes1.animate.set_opacity(0),
            lable1.animate.set_opacity(0),
        )

        self.wait()





#
class Multiple2DRelative0012(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))

        rad = -30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(ApplyMethod(axes1.apply_matrix, matrix_y))

        self.play(axes1.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.8, run_time=2)

        dot = Dot3D(point=[4, -4, 1], depth_test=False)

        arrow1 = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[4, -4, 1], depth_test=False)

        arrow2 = OpenGLArrow3D(start=np.array([2, 2, 2]), end=[4, -4, 1], depth_test=False).set_color(YELLOW)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(dot))

        labes = MathTex(r"P(4,-4,1)").scale(0.5)
        labes.shift([4, -4, 1])
        self.add_fixed_orientation_mobjects(labes)

        arrow_t = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[2, 2, 2])
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
        \end{bmatrix} """).scale(0.8)

        matrix2 = MathTex(r"""
        M =
        \begin{bmatrix} 
        cos(30) & -sin(30) &0 \\ 
        sin(30) & cos(30) &0\\
        0 & 0 &1
        \end{bmatrix} """).set_color(YELLOW).scale(0.55)

        self.add_fixed_in_frame_mobjects(matrix.to_corner(UL))

        self.add_fixed_in_frame_mobjects(matrix2.next_to(matrix, DOWN))

        self.wait(3)


class Multiple2DRelative0022(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))

        rad = -30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(ApplyMethod(axes1.apply_matrix, matrix_y))

        self.play(axes1.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.8, run_time=2)

        dot = Dot3D(point=[4, -4, 1], depth_test=False)

        arrow1 = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[4, -4, 1], depth_test=False)

        arrow2 = OpenGLArrow3D(start=np.array([2, 2, 2]), end=[4, -4, 1], depth_test=False).set_color(YELLOW)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(dot))

        labes = MathTex(r"P(4,-4,1)").scale(0.5)
        labes.shift([4, -4, 1])
        self.add_fixed_orientation_mobjects(labes)

        arrow_t = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[2, 2, 2])
        self.play(Create(arrow_t))

        # matrix = MathTex(r"""
        # M
        # =
        # \begin{bmatrix}
        # 1 & 0& 0\\
        # 0 & 1& 0\\
        # 0 & 0& 1
        # \end{bmatrix} """).scale(0.8)
        #
        # matrix2 = MathTex(r"""
        # M =
        # \begin{bmatrix}
        # cos(30) & -sin(30) &0 \\
        # sin(30) & cos(30) &0\\
        # 0 & 0 &1
        # \end{bmatrix} """).set_color(YELLOW).scale(0.55)
        #
        # self.add_fixed_in_frame_mobjects(matrix.to_corner(UL))
        #
        # self.add_fixed_in_frame_mobjects(matrix2.next_to(matrix, DOWN))

        rad = -60 * DEGREES
        matrix_y1 = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])

        axes2 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes2.add(axes2.get_axis_labels())
        axes2.set_color(RED)
        self.play(Create(axes2))
        self.play(ApplyMethod(axes2.apply_matrix, matrix_y1))
        self.play(axes2.animate.shift([-2, -2, 2]))

        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(1)


class Multiple2DRelative0032(ThreeDScene):
    def construct(self):
        self.next_section(skip_animations=False)
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        axes.add(axes.get_axis_labels())
        number_plane = NumberPlane(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],
                                   x_length=14, y_length=14, z_length=8)
        self.play(Create(number_plane))
        self.play(Create(axes))

        axes1 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes1.add(axes1.get_axis_labels())
        axes1.set_color(YELLOW)
        self.play(Create(axes1))

        rad = -30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        self.play(ApplyMethod(axes1.apply_matrix, matrix_y))

        self.play(axes1.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.8, run_time=2)

        dot = Dot3D(point=[4, -4, 1], depth_test=False)

        arrow1 = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[4, -4, 1], depth_test=False)

        arrow2 = OpenGLArrow3D(start=np.array([2, 2, 2]), end=[4, -4, 1], depth_test=False).set_color(YELLOW)

        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(dot))

        labes = MathTex(r"P(4,-4,1)").scale(0.5)
        labes.shift([4, -4, 1])
        self.add_fixed_orientation_mobjects(labes)

        arrow_t = OpenGLArrow3D(start=np.array([0, 0, 0]), end=[2, 2, 2])
        self.play(Create(arrow_t))

        rad = -60 * DEGREES
        matrix_y1 = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        pitchRad = 36.7 * DEGREES
        matrix_z = np.array([
            [np.cos(pitchRad), 0, np.sin(pitchRad)],
            [0, 1, 0],
            [-np.sin(pitchRad), 0, np.cos(pitchRad)]
        ]);

        axes2 = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
                           x_length=6,
                           y_length=6, z_length=6)

        axes2.add(axes2.get_axis_labels())
        axes2.set_color(RED)
        self.play(Create(axes2))
        self.play(ApplyMethod(axes2.apply_matrix, matrix_y1 @ matrix_z))
        self.play(axes2.animate.move_to([-2, -2, 2]))
        self.wait(1)
        self.next_section(skip_animations=False)

        animate = axes1.animate.apply_matrix(about_point=axes1.get_center(), matrix=matrix_y.T)
        self.play(animate)
        self.wait(1)
        animate = axes1.animate.apply_matrix(about_point=axes1.get_center(), matrix=matrix_y1 @ matrix_z)
        self.play(animate)
        self.wait(1)
        self.play(axes1.animate.move_to([-2, -2, 2]))

        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(1)


with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    Multiple2DRelative001().render()
    exit(1)
