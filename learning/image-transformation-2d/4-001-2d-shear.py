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

class Shear001(ThreeDScene):
    config.output_file = "Shear001-水平.mp4"

    def construct(self):
        latex_str1 = r"""
            \begin{bmatrix} x' \\ y' \end{bmatrix}
            =
            \begin{bmatrix} 1 & s \\ 0 & 1 \end{bmatrix}
            \cdot
            \begin{bmatrix} x \\ y \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))

        latex_str2 = r"""
            \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}
           \cdot
        """
        math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        matrix = np.array([
            [1, 2, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        new_points = matrix @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))

class Shear002(ThreeDScene):
    config.output_file = "Shear002-垂直.mp4"

    def construct(self):
        latex_str1 = r"""
                   \begin{bmatrix} x' \\ y' \end{bmatrix}
                   =
                   \begin{bmatrix} 1 & s \\ 0 & 1 \end{bmatrix}
                   \cdot
                   \begin{bmatrix} x \\ y \end{bmatrix}
                """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))

        latex_str2 = r"""
          \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
           \cdot
        """
        math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))


        matrix = np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 0, 1]
        ])
        new_points = matrix @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))

class Shear003(ThreeDScene):
    config.output_file = "Shear003-水平和垂直.mp4"

    def construct(self):
        latex_str1 = r"""
            \begin{bmatrix} x' \\ y' \end{bmatrix}
           =
           \begin{bmatrix} 1 & s \\ t & 1 \end{bmatrix}
           \cdot
           \begin{bmatrix} x \\ y \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))

        latex_str2 = r"""
           \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}
           \cdot
        """
        math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        matrix = np.array([
            [1, 2, 0],
            [2, 1, 0],
            [0, 0, 1]
        ])
        new_points = matrix @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))

class Shear004(ThreeDScene):
    config.output_file = "Shear004-坍缩.mp4"

    def construct(self):
        latex_str1 = r"""
            \begin{bmatrix} x' \\ y' \end{bmatrix}
           =
           \begin{bmatrix} 1 & s \\ t & 1 \end{bmatrix}
           \cdot
           \begin{bmatrix} x \\ y \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.025, stroke_width=2)
        self.play(Create(image))

        self.play(Create(Axes(tips=True,include_numbers=False)))

        latex_str2 = r"""
           \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}
           \cdot
        """
        math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        # self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        matrix1 = np.array([
            [1, 2, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        matrix2 = np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 0, 0]
        ])
        matrix3 =matrix2 + matrix1

        obj = Matrix(matrix3.tolist()).scale(0.7)
        self.play(Create(obj.next_to(math_tex1, direction=DOWN)))


        new_points = matrix3 @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))

with tempconfig({"preview": True, "renderer": "opengl"}):
    Shear004().render()
    exit(1)