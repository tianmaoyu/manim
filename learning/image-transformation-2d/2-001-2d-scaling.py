
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


#放大两倍
class Scaling001(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part=image_array[50:150,50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)

        self.play(Create(image))
        text= MathTex(r" \times 2").scale(3).next_to(image,direction=RIGHT)
        self.play(Create(text))
        self.wait()

        new_points=image.points * 2
        self.play(FadeOut(text),ApplyMethod(image.set_points, new_points))





#缩小
class Scaling002(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)

        self.play(Create(image))
        text = MathTex(r" \times 0.5").scale(3).next_to(image, direction=RIGHT)
        self.play(Create(text))
        self.wait()

        new_points = image.points * 0.5
        self.play(FadeOut(text), ApplyMethod(image.set_points, new_points))


class Scaling003(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image_array_part = image_array[50:150, 50:150]
        image = NumpyImage(image_array=image_array_part, distance=0.05, stroke_width=2)

        self.play(Create(image))
        text = MathTex(r" \times -1").scale(3).next_to(image, direction=RIGHT)
        self.play(Create(text))

        new_points = image.points * -1
        self.play(FadeOut(text), ApplyMethod(image.set_points, new_points))
        self.wait()


#等比缩放
class Scaling004(ThreeDScene):
    config.output_file = "Scaling004-等比缩放.mp4"
    def construct(self):

        latex_str = r"""
        \begin{bmatrix}
        x'\\
        y'
        \end{bmatrix}
        =
        a \times
        \begin{bmatrix}
        x\\
        y
        \end{bmatrix}
        """
        math_tex = MathTex(latex_str)
        self.play(Create(math_tex))
        self.play(math_tex.animate.to_corner(UL))


        image = np.zeros((50, 50, 4), dtype=np.uint8)
        image[:, :, 0] = 255
        image[:, :, 3] = 255
        image = NumpyImage(image_array=image, distance=0.05, stroke_width=2)
        self.play(Create(image))

        axes = Axes(x_range=[-7, 7, 1], include_numbers=False, y_range=[-5, 5, 1], x_length=14, y_length=10)
        self.play(Create(axes))

        text = MathTex(r" \times 2").scale(3).next_to(image, direction=RIGHT)
        self.play(Create(text))

        new_points = image.points * 2
        self.play(FadeOut(text), ApplyMethod(image.set_points, new_points))


#非等比缩放
class Scaling005(ThreeDScene):
    config.output_file="Scaling005-非等比缩放.mp4"

    def construct(self):

        latex_str = r"""
        \begin{bmatrix}
        x'\\
        y'
        \end{bmatrix}
        =
        \begin{bmatrix}
        a&0\\
        0&b
        \end{bmatrix}
        \cdot
        \begin{bmatrix}
        x\\
        y
        \end{bmatrix}
        """
        math_tex = MathTex(latex_str)
        self.play(Create(math_tex))
        self.play(math_tex.animate.to_corner(UL))

        axes = Axes(x_range=[-7, 7, 1], include_numbers=False, y_range=[-5, 5, 1], x_length=14, y_length=10)
        self.play(Create(axes))

        image = np.zeros((50, 50, 4), dtype=np.uint8)
        image[:, :, 0] = 255
        image[:, :, 3] = 255
        image = NumpyImage(image_array=image, distance=0.05, stroke_width=2)
        self.play(Create(image))

        math_tex2 = r"""
                   \begin{bmatrix}
                    1.5&0\\
                    0&0.5
                   \end{bmatrix}
                    \cdot
                   """
        text = MathTex(math_tex2).to_corner(corner=UR)
        self.play(Create(text))

        scale_matrix = np.array([
            [1.5, 0, 0],
            [0, 0.5, 0],
            [0, 0, 1]
        ])
        new_points = scale_matrix @ image.points.T
        new_points= new_points.T
        self.play(ApplyMethod(image.set_points, new_points))


with tempconfig({"preview": True,  "renderer": "opengl"}):
    Scaling005().render()
    exit(1)