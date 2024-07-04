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


#
class  Vector_Subtraction_to_Matrix_Multipliction(ThreeDScene):
    def construct(self):

        matrix = MathTex(r""" 
       \begin{bmatrix}
x-x'\\y-y'\\z-z'
\end{bmatrix}
=
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
-
\begin{bmatrix}
x'\\y'\\z'
\end{bmatrix}
        """,tex_template=TexTemplateLibrary.ctex)

        self.add(matrix.to_corner(UP))

        matrix2 = MathTex(r"""
\begin{bmatrix}
x-x'\\y-y'\\z-z' \\1
\end{bmatrix}
=
\begin{bmatrix}
1&0&0&-x'\\0&1&0&-y'\\0&0&1&-z'\\0&0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\y\\z \\1
\end{bmatrix}
                """,tex_template=TexTemplateLibrary.ctex)

        self.add(matrix2.next_to(matrix,direction=DOWN,aligned_edge=LEFT))

class  Vector_Add_to_Matrix_Multipliction(ThreeDScene):
    def construct(self):

        matrix = MathTex(r""" 
       \begin{bmatrix}
x+x'\\y+y'\\z+z'
\end{bmatrix}
=
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
+
\begin{bmatrix}
x'\\y'\\z'
\end{bmatrix}
        """,tex_template=TexTemplateLibrary.ctex)

        self.add(matrix.to_corner(UP))

        matrix2 = MathTex(r"""
\begin{bmatrix}
x+x'\\y+y'\\z+z' \\1
\end{bmatrix}
=
\begin{bmatrix}
1&0&0&x'\\0&1&0&y'\\0&0&1&z'\\0&0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\y\\z \\1
\end{bmatrix}
                """,tex_template=TexTemplateLibrary.ctex)

        self.add(matrix2.next_to(matrix,direction=DOWN,aligned_edge=LEFT))

class  Add_vs_Sub_Inverse(ThreeDScene):
    def construct(self):

        matrix = MathTex(r""" 
T=\begin{bmatrix}
1 & 0 & 0 & x\\
0 & 1 & 0 & y\\
0 & 0 & 1 & z\\
0 & 0 & 0 & 1 
\end{bmatrix}
=>
T^{-1}
=\begin{bmatrix}
1 & 0 & 0 & -x\\
0 & 1 & 0 & -y\\
0 & 0 & 1 & -z\\
0 & 0 & 0 & 1 
\end{bmatrix}
        """,tex_template=TexTemplateLibrary.ctex)

        self.add(matrix)

# example,sample

class Case_2D_Rotation_Vector_ADD_Sub(ThreeDScene):
    def construct(self):
        latex_str1 = r"""
                \begin{bmatrix} x'\\y'\end{bmatrix}
                =
                \begin{bmatrix} cos(30) & -sin(30) \\ sin(30) & cos(30) \end{bmatrix}
                \left(
                \begin{bmatrix} x\\y\end{bmatrix}
                -
                \begin{bmatrix}  2\\  2 \end{bmatrix}
                \right)
                +
                \begin{bmatrix}  2\\  2 \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        # image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=1,depth_test=False)
        self.play(Create(image))

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        self.play(Create(axes))
        #
        # latex_str2 = r"""
        #   \begin{bmatrix} cos(30) & -sin(30) \\ sin(30) & cos(30)\end{bmatrix}
        #    \cdot
        # """
        # math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        # self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        mover_vector = np.array([2, 2, 0])
        dot=Dot(point=mover_vector,color=YELLOW)
        self.add(dot)
        line=DashedLine(start=ORIGIN,end=mover_vector,color=YELLOW)
        self.play(Create(line),Create(line.copy()))


        rad=30*DEGREES
        matrix = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        new_points =(matrix @ (image.points - mover_vector).T).T +mover_vector

        line_animate = line.animate.rotate(30 * DEGREES, about_point=mover_vector)
        arc= Arc(start_angle=225*DEGREES,angle=30*DEGREES,arc_center=mover_vector)
        self.play(ApplyMethod(image.set_points, new_points),line_animate,Create(arc))


class Case_Vector_Transfrom_Multiplication(ThreeDScene):
    def construct(self):
        latex_str1 = r"""
                \begin{bmatrix} x\\y\\1 \end{bmatrix}
=
\begin{bmatrix} 1&0&2\\0&1&2\\0&0&1\end{bmatrix}
\begin{bmatrix} 
cos(30) & -sin(30) &0 \\
sin(30) & cos(30) &0 \\
0&0&1
\end{bmatrix}
\begin{bmatrix} 1&0&-2\\0&1&-2\\0&0&1\end{bmatrix}
\begin{bmatrix}  x\\  y\\1 \end{bmatrix}
           """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        # image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=1, depth_test=False)
        self.play(Create(image))

        axes = ThreeDAxes(include_numbers=False, x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1], x_length=6,
                          y_length=6, z_length=6)
        self.play(Create(axes))
        #
        # latex_str2 = r"""
        #   \begin{bmatrix} cos(30) & -sin(30) \\ sin(30) & cos(30)\end{bmatrix}
        #    \cdot
        # """
        # math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        # self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        mover_vector = np.array([2, 2, 0])
        dot = Dot(point=mover_vector, color=YELLOW)
        self.add(dot)
        line = DashedLine(start=ORIGIN, end=mover_vector, color=YELLOW)
        self.play(Create(line), Create(line.copy()))

        rad = 30 * DEGREES
        matrix = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        matrix2 = np.array([
            [1, 0, 2],
            [0, 1, 2],
            [0, 0, 1]
        ])
        matrix3 = np.array([
            [1, 0, -2],
            [0, 1, -2],
            [0, 0, 1]
        ])
        points= image.points.copy()
        points[:,2]=1
        new_points = (matrix2 @matrix @ matrix3 @ points.T).T

        line_animate = line.animate.rotate(30 * DEGREES, about_point=mover_vector)
        arc = Arc(start_angle=225 * DEGREES, angle=30 * DEGREES, arc_center=mover_vector)
        self.play(ApplyMethod(image.set_points, new_points), line_animate, Create(arc))


with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    Case_Vector_Transfrom_Multiplication().render()
    exit(1)
