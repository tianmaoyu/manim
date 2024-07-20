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

        axes1.add(axes1.get_axis_labels(x_label="x'",y_label="y'"))
        axes1.set_color(YELLOW)
        dot1 = Dot(point=[2, 0.5, 0], color=YELLOW)
        lable1 = MarkupText("P'(2,0.5)").set_color(YELLOW).scale(0.3)
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


        # self.play(
        #     axes.animate.set_opacity(0),
        #     lable.animate.set_opacity(0),
        #     FadeIn(arrow),
        # )

        matrix = MathTex(r"""
               M=
               \begin{bmatrix}
               1 & 0 \\
               0 & 1 
               \end{bmatrix}""",tex_template=TexTemplateLibrary.ctex)

        matrix2 = MathTex(r"""
               M' =
               \begin{bmatrix} 
               cos(\theta) & -sin(\theta) \\ 
               sin(\theta) & cos(\theta) 
               \end{bmatrix} """,tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)

        self.play(
            Create(matrix.to_corner(UL)),
            Create(matrix2.next_to(matrix,direction=DOWN,aligned_edge=LEFT)),
        )

        self.wait()

        # self.play(
        #     axes.animate.set_opacity(1),
        #     lable.animate.set_opacity(1),
        #     axes1.animate.set_opacity(0),
        #     lable1.animate.set_opacity(0),
        # )

        # self.wait()


class Multiple2DRelative002(ThreeDScene):
    def construct(self):
        self.move_camera(zoom=0.8)
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

        axes1.add(axes1.get_axis_labels(x_label="x'",y_label="y'"))
        axes1.set_color(YELLOW)
        dot1 = Dot(point=[2, 0.5, 0], color=YELLOW)
        lable1 = MarkupText("P'(2,0.5)").set_color(YELLOW).scale(0.3)
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


        matrix = MathTex(r"""
               M=
               \begin{bmatrix}
               1 & 0 \\
               0 & 1 
               \end{bmatrix}""",tex_template=TexTemplateLibrary.ctex)

        matrix2 = MathTex(r"""
               M' =
               \begin{bmatrix} 
               cos(\theta) & -sin(\theta) \\ 
               sin(\theta) & cos(\theta) 
               \end{bmatrix} """,tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)

        self.play(
            Create(matrix.to_corner(UL+LEFT)),
            Create(matrix2.next_to(matrix,direction=DOWN,aligned_edge=LEFT)),
        )

        self.wait()



        self.play(
            axes1.animate.shift([2,2,0]),
            lable1.animate.shift([2,2,0]),
            dot1.animate.shift([2,2,0]),

        )
        dot_o1 = Dot(point=ORIGIN)
        lable_o1 = MarkupText("O(0,0)").scale(0.3)
        lable_o1.next_to(dot_o1, RIGHT, buff=0.1)

        dot_o2 = Dot(point=[2, 2, 0], color=YELLOW)
        lable_o2 = MarkupText("O'(2,2)").set_color(YELLOW).scale(0.3)
        lable_o2.next_to(dot_o2, RIGHT, buff=0.1)

        self.add(dot_o1,lable_o1,dot_o2,lable_o2)

        # arrow = OpenGLArrow3D(start=ORIGIN, end=dot_o2.get_center())
        # self.play(Create(arrow))

        self.wait()

# 一些图片
class Multiple2D_Image(ThreeDScene):
    def construct(self):

        matrix = MathTex(r""" Matrix=TR_iRT^{-1}""",tex_template=TexTemplateLibrary.ctex)

        self.add(matrix.set_color(YELLOW).scale(2))

        matrix2 = MathTex(r"""
               M' =
               \begin{bmatrix} 
               cos(\theta) & -sin(\theta) \\ 
               sin(\theta) & cos(\theta) 
               \end{bmatrix} """,tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)
class Multiple2D_Image2(ThreeDScene):
    def construct(self):

        matrix = MathTex(r""" Matrix=TR_iRT^{-1}""",tex_template=TexTemplateLibrary.ctex)

        self.add(matrix.set_color(YELLOW).scale(2))

        matrix2 = MathTex(r"""
               M' =
               \begin{bmatrix} 
               cos(\theta) & -sin(\theta) \\ 
               sin(\theta) & cos(\theta) 
               \end{bmatrix} """,tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)


with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    Multiple2DRelative002().render()
    exit(1)
