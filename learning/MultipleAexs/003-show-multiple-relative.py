from manim import *
from manim.mobject.geometry.tips import ArrowTriangleFilledTipSmall
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
                \begin{bmatrix} x'\\y'\\1 \end{bmatrix}
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

class Right_Left_Multipliaction_Transfromer_Order(ThreeDScene):
    def construct(self):
        latex_str1 = r"""
   \begin{bmatrix}
x'\\y'
\end{bmatrix}
= A \left(B\left(C\begin{bmatrix}x\\y\end{bmatrix}\right)\right)
=ABC 
\begin{bmatrix}x\\y\end{bmatrix}
                   """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UP))

        text1 = MarkupText("注意顺序和读发", font_size=44)
        text2 = MarkupText("1:先进行C变换", font_size=33)
        text3 = MarkupText("2:再进行B变换",  font_size=33)
        text4 = MarkupText("3:最后进行A变换",  font_size=33)
        group = VGroup(text1, text2, text3, text4).arrange(DOWN)
        self.play(FadeIn(group))


class Three_Two_Dimensional_coordinate_systems(ThreeDScene):
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

        axes1.add(axes1.get_axis_labels(x_label="x'", y_label="y'"))
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
        return

        self.move_camera(zoom=0.8)
        matrix = MathTex(r"""
                       M=
                       \begin{bmatrix}
                       1 & 0 \\
                       0 & 1 
                       \end{bmatrix}""", tex_template=TexTemplateLibrary.ctex)

        matrix2 = MathTex(r"""
                       M' =
                       \begin{bmatrix} 
                       cos(\theta) & -sin(\theta) \\ 
                       sin(\theta) & cos(\theta) 
                       \end{bmatrix} """, tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)

        self.play(
            Create(matrix.to_corner(UL + LEFT)),
            Create(matrix2.next_to(matrix, direction=DOWN, aligned_edge=LEFT)),
        )

        self.wait()

        self.play(
            axes1.animate.shift([2, 2, 0]),
            lable1.animate.shift([2, 2, 0]),
            dot1.animate.shift([2, 2, 0]),

        )
        dot_o1 = Dot(point=ORIGIN)
        lable_o1 = MarkupText("O(0,0)").scale(0.3)
        lable_o1.next_to(dot_o1, RIGHT, buff=0.1)

        dot_o2 = Dot(point=[2, 2, 0], color=YELLOW)
        lable_o2 = MarkupText("O'(2,2)").set_color(YELLOW).scale(0.3)
        lable_o2.next_to(dot_o2, RIGHT, buff=0.1)

        self.add(dot_o1, lable_o1, dot_o2, lable_o2)
class ThreeDAexs_Matrix_Base_Vector(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=35 * DEGREES)

        axes = ThreeDAxes(include_numbers=False, axis_config={"include_ticks": False}, x_range=[-4, 4, 1],
                          y_range=[-4, 4, 1], z_range=[-3, 3, 1], x_length=8,
                          y_length=8, z_length=6)
        axes.add(axes.get_axis_labels())

        # 创建基向量
        e1 = Vector([2, 0, 0], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)
        e2 = Vector([0, 2, 0], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)
        e3 = Vector([0, 0, 2], color=RED, stroke_width=3.5, tip_shape=ArrowTriangleFilledTipSmall)

        # 添加标签
        e1_label = MathTex("e_1").next_to(e1, UP + RIGHT, buff=0).scale(1).set_color(RED)
        e2_label = MathTex("e_2").next_to(e2, LEFT + UP, buff=0).scale(1).set_color(RED)
        e3_label = MathTex("e_3").next_to(e3, OUT, buff=0).scale(1).set_color(RED)
        self.add(axes)

        self.play(Create(e1), Create(e2), Create(e3))
        self.add(e1, e1_label, e2, e2_label, e3, e3_label)

        self.wait()

        start_dot = Dot3D(point=[0, 0, 0], color=BLUE)
        end_dot = Dot3D([2, 2, 2], color=BLUE)
        self.play(Create(start_dot), Create(end_dot))

        start_dot_lables = MathTex("O(x_o,y_o,z_o)").scale(0.4)

        start_dot_lables.next_to(start_dot)
        self.add_fixed_orientation_mobjects(start_dot_lables)
        self.add(start_dot_lables)

        end_dot_lables = MathTex("P(x,y,z)").scale(0.4)

        end_dot_lables.next_to(end_dot)
        self.add_fixed_orientation_mobjects(end_dot_lables)
        self.add(end_dot_lables)

        vector = OpenGLArrow3D(start=[0, 0, 0], end=[2, 2, 2], color=BLUE)
        self.play(FadeIn(vector))
        self.wait(1)

        tex1 = MathTex(r"""
   \vec{OP}= x\vec{e_1} +y\vec{e_2}+z\vec{e_3}
            """)
        tex1.fix_in_frame()
        tex2 = MathTex(r"""
          \vec{OP}= \begin{bmatrix} \vec{e_1}&\vec{e_2}&\vec{e_3} \end{bmatrix}
\begin{bmatrix} x \\ y\\ z \end{bmatrix}
                    """)
        tex2.fix_in_frame()

        tex3 = MathTex(r"""
         \vec{OP}= \begin{bmatrix} 
e_{1x} & e_{2x} & e_{3x}\\
e_{1y} & e_{2y} & e_{3y}\\
e_{1z} & e_{2z} & e_{3z}
\end{bmatrix}
\begin{bmatrix} x \\ y\\ z \end{bmatrix}
                    """)

        tex3.fix_in_frame()
        self.play(Write(tex1.scale(0.8).to_corner(UL)))
        self.play(Write(tex2.scale(0.8).next_to(tex1,direction=DOWN, aligned_edge=LEFT)))
        self.play(Write(tex3.scale(0.8).next_to(tex2,direction=DOWN,aligned_edge=LEFT)))

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2)


with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    ThreeDAexs_Matrix_Base_Vector().render()
    exit(1)
