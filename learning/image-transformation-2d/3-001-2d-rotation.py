from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image


# 旋转
class Rotation000(ThreeDScene):
    def construct(self):
        # 设置坐标系
        axes = Axes(x_range=(-3, 3, 1), y_range=(-3, 3, 1))
        axes.add(axes.get_axis_labels())
        # 画圆，半径为2
        circle = Circle(radius=2, color=BLUE)
        self.add(axes, circle)

        # 初始化点P在圆周上的位置，假设初始θ=0 # 初始角度，例如45度
        start_rad = PI / 4
        end_rad = PI / 2

        point_start = circle.point_from_proportion(start_rad / TAU)
        dot = Dot(point=point_start, color=YELLOW)
        vector_start = Vector(point_start, stroke_width=1)
        start_matrix= vector_start.coordinate_label()
        arc_start = Arc(radius=0.5, start_angle=0, angle=start_rad, color=PURPLE)
        start_label = MathTex(r"\theta").scale(0.7).next_to(arc_start, UR, buff=0.15)


        self.add(vector_start, arc_start, start_label, dot,start_matrix)

        self.wait(1)

        # 旋转动画
        vector_end = vector_start.copy()
        dot_end = dot.copy()

        self.play(Rotate(vector_end, angle=end_rad, about_point=circle.get_center()),
                  Rotate(dot_end, angle=end_rad, about_point=circle.get_center()),
                  run_time=2)

        arc_end = Arc(radius=1, start_angle=start_rad, angle=end_rad, color=YELLOW)
        end_label = MathTex(r"\alpha").scale(0.7).next_to(arc_end, UP, buff=0.15)
        end_matrix=vector_end.coordinate_label()
        self.add(arc_end, end_label,end_matrix)
        self.wait(1)








# 和差公式
class Rotation001(ThreeDScene):
    def construct(self):

        tex=MathTex(r"cos(\alpha+\beta)=cos\alpha\cdot cos\beta - sin\alpha\cdot sin\beta\\"
                    r"cos(\alpha-\beta)=cos\alpha\cdot cos\beta + sin\alpha\cdot sin\beta\\"
                    r"\sin(\alpha\pm\beta)=\sin\alpha\cdot\cos\beta\pm\cos\alpha\cdot\sin\beta")
        self.play(Write(tex))

        brace = Brace(tex, direction=LEFT)
        self.play(FadeIn(brace))
        # # 创建并排列数学公式
        # tex1 = MarkupText(r"cos(α+β)=cosα·cosβ - sinα·sinβ",tex_template=TexTemplateLibrary.ctex)
        # tex2 = MarkupText(r"cos(α-β)=cosα·cosβ + sinα·sinβ",tex_template=TexTemplateLibrary.ctex)
        # tex3 = MarkupText(r"sin(α±β)=sinα·cosβ ± cosα·sinβ",tex_template=TexTemplateLibrary.ctex)
        #
        # # 对齐公式
        # tex2.next_to(tex1, DOWN)
        # tex3.next_to(tex2, DOWN)
        #
        # # 添加公式到场景，并带有入场动画
        # self.play(Create(tex1), run_time=2)
        # self.wait(1)  # 等待一段时间后显示下一个公式
        # self.play(Create(tex2), run_time=2)
        # self.wait(1)  # 同样等待
        # self.play(Create(tex3), run_time=2)

# x,y 的方程组
class Rotation002(ThreeDScene):
    def construct(self):

        tex=MathTex(r"x' &= \cos(\alpha + \beta) = \cos\alpha \cos\beta - \sin\alpha \sin\beta = x\cos\alpha - y\sin\alpha\\"
                    r"y' &= \sin(\alpha + \beta) = \sin\alpha \cos\beta + \cos\alpha \sin\beta = x\sin\alpha + y\cos\alpha")
        tex.shift(UP)
        self.play(Write(tex))

        brace = Brace(tex, direction=LEFT)
        self.play(FadeIn(brace))

        tex1=MathTex(r"x' &= x\cos\alpha - y\sin\alpha\\"
                    r"y' &= x\sin\alpha + y\cos\alpha")
        tex1.next_to(tex,direction=DOWN)
        brace1 = Brace(tex1, direction=LEFT)

        self.play(Write(tex1),FadeIn(brace1))

        # # 创建并排列数学公式
        # tex1 = MarkupText(r"cos(α+β)=cosα·cosβ - sinα·sinβ",tex_template=TexTemplateLibrary.ctex)
        # tex2 = MarkupText(r"cos(α-β)=cosα·cosβ + sinα·sinβ",tex_template=TexTemplateLibrary.ctex)
        # tex3 = MarkupText(r"sin(α±β)=sinα·cosβ ± cosα·sinβ",tex_template=TexTemplateLibrary.ctex)
        #
        # # 对齐公式
        # tex2.next_to(tex1, DOWN)
        # tex3.next_to(tex2, DOWN)
        #
        # # 添加公式到场景，并带有入场动画
        # self.play(Create(tex1), run_time=2)
        # self.wait(1)  # 等待一段时间后显示下一个公式
        # self.play(Create(tex2), run_time=2)
        # self.wait(1)  # 同样等待
        # self.play(Create(tex3), run_time=2)



# 逆时针旋转矩阵矩阵
class Rotation003(ThreeDScene):
    def construct(self):

        tex1=MathTex(r"x' &= x\cos\alpha - y\sin\alpha\\"
                    r"y' &= x\sin\alpha + y\cos\alpha")
        tex1.to_corner(UP)
        brace1 = Brace(tex1, direction=LEFT)
        self.play(Write(tex1),FadeIn(brace1))

        tex2 = MathTex(r'''
        \begin{bmatrix}
cos(\alpha) & -sin(\alpha) \\
sin(\alpha) & cos(\alpha)
\end{bmatrix}
\cdot \begin{bmatrix} x \\ y \end{bmatrix} 
= \begin{bmatrix} x' \\ y' \end{bmatrix}
        ''')
        tex2.next_to(tex1,direction=DOWN*2)
        self.play(Write(tex2))

        tex3 = MathTex(r'''
R=
\begin{bmatrix}
cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta)
\end{bmatrix}
                ''')
        tex3.next_to(tex2, direction=DOWN*2)
        self.play(Write(tex3))

        # # 创建并排列数学公式
        # tex1 = MarkupText(r"cos(α+β)=cosα·cosβ - sinα·sinβ",tex_template=TexTemplateLibrary.ctex)
        # tex2 = MarkupText(r"cos(α-β)=cosα·cosβ + sinα·sinβ",tex_template=TexTemplateLibrary.ctex)
        # tex3 = MarkupText(r"sin(α±β)=sinα·cosβ ± cosα·sinβ",tex_template=TexTemplateLibrary.ctex)
        #
        # # 对齐公式
        # tex2.next_to(tex1, DOWN)
        # tex3.next_to(tex2, DOWN)
        #
        # # 添加公式到场景，并带有入场动画
        # self.play(Create(tex1), run_time=2)
        # self.wait(1)  # 等待一段时间后显示下一个公式
        # self.play(Create(tex2), run_time=2)
        # self.wait(1)  # 同样等待
        # self.play(Create(tex3), run_time=2)



with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Rotation003().render()
    exit(1)
