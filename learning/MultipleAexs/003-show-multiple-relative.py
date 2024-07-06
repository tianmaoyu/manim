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
        # axes.add(axes.get_axis_labels())

        dot = Dot(point=[2, 0.5, 0])
        lable = MarkupText("P(2,0.5)").scale(0.3)
        lable.next_to(dot, RIGHT, buff=0.1)
        self.add(lable)
        self.play(FadeIn(axes), FadeIn(dot), FadeIn(lable))

        self.wait()

        axes1 = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                     y_length=8, z_length=6)

        # axes1.add(axes1.get_axis_labels(x_label="x'", y_label="y'"))
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

        axes2 = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                     y_length=8, z_length=6)

        # axes2.add(axes2.get_axis_labels(x_label="x''", y_label="y''"))
        axes2.set_color(BLUE)
        dot2 = Dot(point=[2, 0.5, 0], color=BLUE)
        lable2 = MarkupText("P''(2,0.5)").set_color(BLUE).scale(0.3)
        lable2.next_to(dot2, RIGHT, buff=0.1)

        rad = -30 * DEGREES
        matrix_y = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])

        self.play(
            ApplyMethod(axes2.apply_matrix, matrix_y),
            ApplyMethod(dot2.apply_matrix, matrix_y),
            ApplyMethod(lable2.apply_matrix, matrix_y)
        )

        self.move_camera(zoom=0.7)


        self.wait()

        self.play(
            axes1.animate.shift([2, 2, 0]),
            lable1.animate.shift([2, 2, 0]),
            dot1.animate.shift([2, 2, 0]),

        )

        self.play(
            axes2.animate.shift([3, -2, 0]),
            lable2.animate.shift([3, -2, 0]),
            dot2.animate.shift([3, -2, 0]),

        )

        dot_o1 = Dot(point=ORIGIN)
        lable_o1 = MarkupText("O(0,0)").scale(0.3)
        lable_o1.next_to(dot_o1, RIGHT, buff=0.1)

        dot_o2 = Dot(point=[2, 2, 0], color=YELLOW)
        lable_o2 = MarkupText("O'(2,2)").set_color(YELLOW).scale(0.3)
        lable_o2.next_to(dot_o2, RIGHT, buff=0.1)

        dot_o3 = Dot(point=[3, -2, 0], color=BLUE)
        lable_o3 = MarkupText("O''(3, -2, 0)").set_color(BLUE).scale(0.3)
        lable_o3.next_to(dot_o3, RIGHT, buff=0.1)

        self.add(dot_o1, lable_o1, dot_o2, lable_o2,dot_o3,lable_o3)

        matrix1 = MathTex(r"""
                            M=
                            \begin{bmatrix}
                            1 & 0 \\
                            0 & 1 
                            \end{bmatrix}""", tex_template=TexTemplateLibrary.ctex)
        matrix2 = MathTex(r"""
                            M' =
                            \begin{bmatrix} 
                            cos(30) & -sin(30) \\ 
                            sin(30) & cos(30) 
                            \end{bmatrix} """, tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)
        matrix3 = MathTex(r"""
                                 M'' =
                                 \begin{bmatrix} 
                                 cos(-30) & -sin(-30) \\ 
                                 sin(-30) & cos(-30) 
                                 \end{bmatrix} """, tex_template=TexTemplateLibrary.ctex).set_color(BLUE)
        matrix1.scale(0.7).fix_in_frame()
        matrix2.scale(0.7).fix_in_frame()
        matrix3.scale(0.7).fix_in_frame()

        self.play(FadeIn(matrix1.to_corner(UL)))
        self.play(FadeIn(matrix2.next_to(matrix1, direction=DOWN, aligned_edge=LEFT)))
        self.play(FadeIn(matrix3.next_to(matrix2, direction=DOWN, aligned_edge=LEFT)))

class Three_Two_Dimensional_Only_Move(ThreeDScene):
    def construct(self):
        axes = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                    y_length=8, z_length=6)
        # axes.add(axes.get_axis_labels())

        dot = Dot(point=[2, 0.5, 0])
        lable = MarkupText("P(2,0.5)").scale(0.3)
        lable.next_to(dot, RIGHT, buff=0.1)
        self.add(lable)
        self.play(FadeIn(axes), FadeIn(dot), FadeIn(lable))

        self.wait()

        axes1 = Axes(include_numbers=False, x_range=[-4, 4, 1], y_range=[-4, 4, 1], z_range=[-4, 4, 1], x_length=8,
                     y_length=8, z_length=6)

        # axes1.add(axes1.get_axis_labels(x_label="x'", y_label="y'"))
        axes1.set_color(YELLOW)
        dot1 = Dot(point=[2, 0.5, 0], color=YELLOW)
        lable1 = MarkupText("P'(2,0.5)").set_color(YELLOW).scale(0.3)
        lable1.next_to(dot1, RIGHT, buff=0.1)

        self.move_camera(zoom=0.7)

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

        matrix1 = MathTex(r"""
                            M=
                            \begin{bmatrix}
                            1 & 0 \\
                            0 & 1 
                            \end{bmatrix}""", tex_template=TexTemplateLibrary.ctex)
        matrix2 = MathTex(r"""
                            M' =
                            \begin{bmatrix} 
                            1 & 0 \\ 
                            0 & 1 
                            \end{bmatrix} """, tex_template=TexTemplateLibrary.ctex).set_color(YELLOW)

        matrix1.scale(0.7).fix_in_frame()
        matrix2.scale(0.7).fix_in_frame()

        self.play(FadeIn(matrix1.to_corner(UL)))
        self.play(FadeIn(matrix2.next_to(matrix1, direction=DOWN, aligned_edge=LEFT)))


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

class Five_Step_Rotation_For_Aexs(ThreeDScene):
    def construct(self):
        self.next_section(skip_animations=True)
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

        axes1.add(axes1.get_axis_labels(x_label=MarkupText("x").scale(0.5), y_label=MarkupText("y").scale(0.5),
                                        z_label=MarkupText("z").scale(0.5)))
        axes1.set_color(YELLOW)

        def uv_func(u, v):
            x = 1
            y = u
            z = v
            return [x, y, z]

        planSurface = OpenGLSurface(uv_func=uv_func, u_range=[-0.4, 0.4], v_range=[-0.3, 0.3],
                                    depth_test=False).set_color(RED).set_opacity(0.5)

        self.play(Create(planSurface))
        self.play(Create(axes1))

        group = Group()
        group.add(planSurface, axes1)


        matrix_init = np.array([
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, -1]
        ])
        self.play(ApplyMethod(group.apply_matrix, matrix_init))

        self.play(group.animate.shift([2, 2, 2]))

        self.move_camera(zoom=0.75, run_time=2)

        yawRad = -34.3 * DEGREES
        pitchRad = -47.4 * DEGREES
        rollRad = 0.0
        Rz = np.array([
            [np.cos(yawRad), -np.sin(yawRad), 0],
            [np.sin(yawRad), np.cos(yawRad), 0],
            [0, 0, 1]
        ]);

        Ry = np.array([
            [np.cos(pitchRad), 0, np.sin(pitchRad)],
            [0, 1, 0],
            [-np.sin(pitchRad), 0, np.cos(pitchRad)]
        ]);

        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(rollRad), -np.sin(rollRad)],
            [0, np.sin(rollRad), np.cos(rollRad)]
        ]);
        self.next_section(skip_animations=False)
        self.wait(2)

        image = self.renderer.get_frame()
        image_mobject = ImagePixelMobject(image=image)
        image_mobject.fix_in_frame()

        self.add(image_mobject.scale(0.5).to_corner(UL))

        animate = group.animate.shift([-2, -2, -2])
        self.play(animate)

        animate = group.animate.apply_matrix(matrix=matrix_init.T)
        self.play(animate)
        # 先还原- 在变换-移动
        animate = group.animate.apply_matrix(matrix= Rx@Ry@Rz)
        self.play(animate)

        animate = group.animate.apply_matrix(matrix=matrix_init)
        self.play(animate)

        self.play(group.animate.shift([2, 2, 2]))
        self.wait()

        image1 = self.renderer.get_frame()
        image_mobject1=ImagePixelMobject(image=image1)
        image_mobject1.fix_in_frame()

        self.add(image_mobject1.scale(0.5).next_to(image_mobject,direction=DOWN))

        box = SurroundingRectangle(image_mobject).fix_in_frame()
        box2 = SurroundingRectangle(image_mobject1).fix_in_frame()
        # box.scale(0.5).to_corner(UL)
        # box2.scale(0.5).next_to(image_mobject, direction=DOWN)
        self.add(box,box2)
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(3)
        #两图对比


class Relative_3d_three_Aexs(ThreeDScene):
    def construct(self):
        pass

class Multiple_Poster_Image(ThreeDScene):
    def construct(self):

        matrix = MathTex(r"""TR_iRR_i^{-1}T^{-1}""",tex_template=TexTemplateLibrary.ctex)
        self.add(matrix.move_to(UP).set_color(YELLOW).scale(3))

        text= Text(f"回退.回退.旋转.还原.还原",font="sans-serif").scale(1.5)
        self.add(text.next_to(matrix,direction=DOWN).set_color(YELLOW))

class Multiple_some_Image_1(ThreeDScene):
    def construct(self):

        matrix = MathTex(r"""\begin{bmatrix}
x-a\\y-b\\z-c
\end{bmatrix}
=
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
-
\begin{bmatrix}
a\\b\\c
\end{bmatrix}""").move_to(UP).set_color(YELLOW).scale(0.8)
        self.play(Create(matrix))

        matrix2 = MathTex(r"""
\begin{bmatrix}
x-a\\y-b\\z-c\\1
\end{bmatrix}
=
\begin{bmatrix}
1&0&0&-a\\0&1&0&-b\\0&0&1&-c\\0&0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\y\\z \\1
\end{bmatrix}
        """).next_to(matrix,direction=DOWN).set_color(YELLOW).scale(0.8)
        self.play(Create(matrix2))
        self.wait()

        # text= Text(f"回退.回退.旋转.还原.还原",font="sans-serif").scale(1.5)
        # self.add(text.next_to(matrix,direction=DOWN).set_color(YELLOW))
class Multiple_some_Image_2(ThreeDScene):
    def construct(self):

        matrix = MathTex(r"""\begin{bmatrix}
x+a\\y+b\\z+c
\end{bmatrix}
=
\begin{bmatrix}
x\\y\\z
\end{bmatrix}
+
\begin{bmatrix}
a\\b\\c
\end{bmatrix}""").move_to(UP).set_color(YELLOW).scale(0.8)
        self.play(Create(matrix))

        matrix2 = MathTex(r"""
\begin{bmatrix}
x+a\\y+b\\z+c\\1
\end{bmatrix}
=
\begin{bmatrix}
1&0&0&a\\0&1&0&b\\0&0&1&c\\0&0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\y\\z \\1
\end{bmatrix}
        """).next_to(matrix,direction=DOWN).set_color(YELLOW).scale(0.8)
        self.play(Create(matrix2))
        self.wait()

        # text= Text(f"回退.回退.旋转.还原.还原",font="sans-serif").scale(1.5)
        # self.add(text.next_to(matrix,direction=DOWN).set_color(YELLOW))

        class Multiple_some_Image_2(ThreeDScene):
            def construct(self):
                matrix = MathTex(r"""\begin{bmatrix}
        x+a\\y+b\\z+c
        \end{bmatrix}
        =
        \begin{bmatrix}
        x\\y\\z
        \end{bmatrix}
        +
        \begin{bmatrix}
        a\\b\\c
        \end{bmatrix}""").move_to(UP).set_color(YELLOW).scale(0.8)
                self.play(Create(matrix))

                matrix2 = MathTex(r"""
        \begin{bmatrix}
        x+a\\y+b\\z+c\\1
        \end{bmatrix}
        =
        \begin{bmatrix}
        1&0&0&a\\0&1&0&b\\0&0&1&c\\0&0&0&1
        \end{bmatrix}
        \begin{bmatrix}
        x\\y\\z \\1
        \end{bmatrix}
                """).next_to(matrix, direction=DOWN).set_color(YELLOW).scale(0.8)
                self.play(Create(matrix2))
                self.wait()

                # text= Text(f"回退.回退.旋转.还原.还原",font="sans-serif").scale(1.5)
                # self.add(text.next_to(matrix,direction=DOWN).set_color(YELLOW))
class Multiple_some_Image_3(ThreeDScene):
    def construct(self):

        matrix = MathTex(r"""
T=\begin{bmatrix}
1 & 0 & 0 & a\\
0 & 1 & 0 & b\\
0 & 0 & 1 & c\\
0 & 0 & 0 & 1 
\end{bmatrix}
=>
T^{-1}=\begin{bmatrix}
1 & 0 & 0 & -a\\
0 & 1 & 0 & -b\\
0 & 0 & 1 & -c\\
0 & 0 & 0 & 1 
\end{bmatrix}
""").move_to(UP).set_color(YELLOW).scale(0.8)
        self.play(Create(matrix))
        self.wait()
        return
class Multiple_some_Image_4(ThreeDScene):
    def construct(self):

        matrix = MathTex(r"""TR_iRR_i^{-1}T^{-1}""",tex_template=TexTemplateLibrary.ctex)
        matrix.move_to(UP).set_color(YELLOW).scale(3)
        self.play(Create(matrix))
        text= Text(f"回退.回退.旋转.还原.还原",font="sans-serif").scale(1.5)
        text.next_to(matrix,direction=DOWN).set_color(YELLOW)
        self.play(Create(text))
        self.wait()
class Multiple_some_Image_5(ThreeDScene):
    def construct(self):
        text= Text(f"坐标系矩阵×坐标=原点到该坐标的向量",font="sans-serif")
        text.set_color(YELLOW)
        self.play(FadeIn(text))
        self.wait()

with tempconfig({"preview": True, "disable_caching": False, "renderer": "opengl"}):
    Multiple_some_Image_5().render()
    exit(1)
