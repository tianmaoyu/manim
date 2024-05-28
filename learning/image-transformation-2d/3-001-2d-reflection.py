
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



class Reflection001(ThreeDScene):
    config.output_file = "Reflection001-镜像x轴翻转.mp4"

    def construct(self):
        latex_str1 = r"""
                    \begin{bmatrix}
                    x'\\
                    y'
                    \end{bmatrix}
                    =
                    \begin{bmatrix}
                    -1&0\\
                    0& 1
                    \end{bmatrix}
                    \cdot
                    \begin{bmatrix}
                    x\\
                    y
                    \end{bmatrix}
                    """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)
        self.play(Create(image))

        latex_str2 = r"""
                               \begin{bmatrix}
                                -1&0\\
                                0&1
                               \end{bmatrix}
                                \cdot
                               """
        math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        scale_matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        new_points = scale_matrix @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))



class Reflection002(ThreeDScene):
    config.output_file = "Reflection002-镜像y轴翻转.mp4"
    def construct(self):

        latex_str1 = r"""
               \begin{bmatrix}
               x'\\
               y'
               \end{bmatrix}
               =
               \begin{bmatrix}
               1&0\\
               0&-
               \end{bmatrix}
               \cdot
               \begin{bmatrix}
               x\\
               y
               \end{bmatrix}
               """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)
        self.play(Create(image))


        latex_str2 = r"""
                          \begin{bmatrix}
                           1&0\\
                           0&-1
                          \end{bmatrix}
                           \cdot
                          """
        math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        scale_matrix = np.array([
            [1, 0, 0],
            [0,-1, 0],
            [0, 0, 1]
        ])
        new_points = scale_matrix @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))





class Reflection003(ThreeDScene):
    config.output_file = "Reflection003-原点翻转.mp4"
    def construct(self):

        latex_str1 = r"""
               \begin{bmatrix}
               x'\\
               y'
               \end{bmatrix}
               =
               \begin{bmatrix}
               -1&0\\
               0&-1
               \end{bmatrix}
               \cdot
               \begin{bmatrix}
               x\\
               y
               \end{bmatrix}
               """
        math_tex1 = MathTex(latex_str1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UR))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)
        self.play(Create(image))


        latex_str2 = r"""
                          \begin{bmatrix}
                           -1&0\\
                           0&-1
                          \end{bmatrix}
                           \cdot
                          """
        math_tex2 = MathTex(latex_str2).to_corner(corner=LEFT)
        self.play(Create(math_tex2.next_to(math_tex1, direction=DOWN)))

        scale_matrix = np.array([
            [-1, 0, 0],
            [0,-1, 0],
            [0, 0, 1]
        ])
        new_points = scale_matrix @ image.points.T
        new_points = new_points.T
        self.play(ApplyMethod(image.set_points, new_points))




with tempconfig({"preview": True, "disable_caching": True, "renderer": "opengl"}):
    Reflection003().render()
    exit(1)