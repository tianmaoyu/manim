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



class Complex001(ThreeDScene):
    config.output_file = "Complex001-绕任意一点旋转-单步.mp4"

    def construct(self):
        latex_str1 = r"""
                \begin{bmatrix} x\\y\end{bmatrix}
                =
                \begin{bmatrix} cos(30) & -sin(30) \\ sin(30) & cos(30) \end{bmatrix}
                \cdot
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
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))
        #
        # latex_str2 = r"""
        #   \begin{bmatrix} cos(30) & -sin(30) \\ sin(30) & cos(30)\end{bmatrix}
        #    \cdot
        # """
        # math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        # self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        #移动
        vector = Vector(direction=[-2, -2])
        vector.add(vector.coordinate_label())
        self.play(Create(vector))
        mover_vector = np.array([2, 2, 0])
        new_points =  image.points-mover_vector
        self.play(ApplyMethod(image.set_points, new_points))
        self.play(FadeOut(vector))


        rad=30*DEGREES
        scale_matrix = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        new_points = scale_matrix @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))

        # 移动
        vector = Vector(direction=[2, 2])
        vector.add(vector.coordinate_label())
        self.play(Create(vector))
        mover_vector = np.array([2, 2, 0])
        new_points = image.points + mover_vector
        self.play(ApplyMethod(image.set_points, new_points))
        self.play(FadeOut(vector))


class Complex002(ThreeDScene):
    config.output_file = "Complex002-绕任意一点旋转-合并.mp4"

    def construct(self):
        latex_str1 = r"""
                \begin{bmatrix} x\\y\end{bmatrix}
                =
                \begin{bmatrix} cos(30) & -sin(30) \\ sin(30) & cos(30) \end{bmatrix}
                \cdot
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
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))
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
        self.play(Create(line))


        rad=30*DEGREES
        matrix = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
        new_points =(matrix @ (image.points - mover_vector).T).T +mover_vector

        line_animate = line.animate.rotate(30 * DEGREES, about_point=mover_vector)
        self.play(ApplyMethod(image.set_points, new_points),line_animate)



class Complex003(ThreeDScene):
    config.output_file = "Complex003-之关于x任意轴翻转-合并.mp4"

    def construct(self):
        latex_str1 = r"""
            \begin{bmatrix} x\\y\end{bmatrix}
            =
            \begin{bmatrix}-1&0\\0&1 \end{bmatrix}
            \cdot
            \left(
            \begin{bmatrix} x\\y\end{bmatrix}
            -
            \begin{bmatrix}  x_c\\  0 \end{bmatrix}
            \right)
            +
            \begin{bmatrix}  x_c\\  0 \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))

        mover_vector = np.array([2, 0, 0])
        dot=Dot(point=mover_vector,color=YELLOW)
        self.add(dot)
        line=DashedLine(start=[2, -5, 0],end=[2, 5, 0],color=YELLOW)
        self.play(Create(line))

        matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        new_points =(matrix @ (image.points - mover_vector).T).T +mover_vector
        self.play(ApplyMethod(image.set_points, new_points))

class Complex004(ThreeDScene):
    config.output_file = "Complex004-之关于y任意轴翻转-合并.mp4"

    def construct(self):
        latex_str1 = r"""
            \begin{bmatrix} x\\y\end{bmatrix}
            =
            \begin{bmatrix}1&0\\0&-1 \end{bmatrix}
            \cdot
            \left(
            \begin{bmatrix} x\\y\end{bmatrix}
            -
            \begin{bmatrix}  0\\  -1 \end{bmatrix}
            \right)
            +
            \begin{bmatrix}  0\\  -1 \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))

        mover_vector = np.array([0, -1, 0])
        dot=Dot(point=mover_vector,color=YELLOW)
        self.add(dot)
        line=DashedLine(start=[-7, -1, 0],end=[7, -1, 0],color=YELLOW)
        self.play(Create(line))

        matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        new_points =(matrix @ (image.points - mover_vector).T).T +mover_vector
        self.play(ApplyMethod(image.set_points, new_points))


class Complex005(ThreeDScene):
    config.output_file = "Complex005-之关于任意直线翻转-合并.mp4"

    def construct(self):
        latex_str1 = r"""
            \begin{bmatrix} x\\y\end{bmatrix}
            =
            \begin{bmatrix}1&0\\0&-1 \end{bmatrix}
            \cdot
            \left(
            \begin{bmatrix} x\\y\end{bmatrix}
            -
            \begin{bmatrix}  0\\  -1 \end{bmatrix}
            \right)
            +
            \begin{bmatrix}  0\\  -1 \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))

        mover_vector = np.array([0, -1, 0])
        dot=Dot(point=mover_vector,color=YELLOW)
        self.add(dot)
        line=DashedLine(start=[-7, -1, 0],end=[7, -1, 0],color=YELLOW)
        self.play(Create(line))

        matrix = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        new_points =(matrix @ (image.points - mover_vector).T).T +mover_vector
        self.play(ApplyMethod(image.set_points, new_points))


class Complex006(ThreeDScene):
    config.output_file = "Complex006-之关于任意直线翻转-合并.mp4"

    def construct(self):
        a=2
        b=3
        c=-6
        line_latex = rf"""
          {a}x+{b}y+{c}=0
         """
        line_latex = MathTex(line_latex)
        self.play(Create(line_latex))
        self.play(line_latex.animate.to_corner(UL))

        self.play(Create(Axes(tips=False, include_numbers=False)))

        line = DashedLine(start=[-7, 20/3, 0], end=[7, -8/3, 0], color=YELLOW)
        self.play(Create(line))


        matrix_latex = r"""
\begin{bmatrix}x'\\y'\end{bmatrix}
=
\begin{bmatrix}
\frac{b^2-a^2}{a^2+b^2} & \frac{-2ab}{a^2+b^2} \\
\frac{2ab}{a^2+b^2} & \frac{a^2-b^2}{a^2+b^2}
\end{bmatrix}
\cdot
\begin{bmatrix}x\\y\end{bmatrix}
+
\begin{bmatrix}
\frac{-2ac}{a^2+b^2}\\
\frac{-2ac}{a^2+b^2}
\end{bmatrix}
         """
        matrix_latex = MathTex(matrix_latex).scale(0.6)
        self.play(Create(matrix_latex))
        self.play(matrix_latex.animate.to_corner(UR))

        matrix_latex1 = r"""
\begin{bmatrix}x' \\y' \end{bmatrix}
=\frac{1}{13}
\times
\left(
    \begin{bmatrix}
    5 & -12\\
    -12 &  -5
    \end{bmatrix}
    \cdot
    \begin{bmatrix}x \\y \end{bmatrix}
    +
    \begin{bmatrix}
    24 \\
    36
    \end{bmatrix}
\right)
        """
        matrix_latex1 = MathTex(matrix_latex1).scale(0.6).next_to(matrix_latex,direction=DOWN)
        self.play(Create(matrix_latex1))


        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        mover_vector=np.array([24/13,36/13,0])
        matrix = np.array([
            [5/13, -12/13, 0],
            [-12/13, -5/13, 0],
            [0, 0, 1]
        ])
        new_points =(matrix @ image.points.T).T+mover_vector
        self.play(ApplyMethod(image.set_points, new_points))

with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Complex006().render()
    exit(1)
