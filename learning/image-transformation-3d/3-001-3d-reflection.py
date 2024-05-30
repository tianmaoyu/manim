

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, ImageBox
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track
from PIL import Image


#x 变成-x
class ThreeDReflection001(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}
=
\begin{bmatrix}-1&0&0\\0&1&0\\0&0&1\end{bmatrix}
\cdot
\begin{bmatrix}x\\y\\z\end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1).scale(0.7)
        self.add_fixed_in_frame_mobjects(math_tex1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))


        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-4, 4, 1], z_range=[-7, 7, 1],   x_length=14, y_length=8, z_length=14)
        axes.add(axes.get_axis_labels())
        self.play(Create(axes))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        imageBox = ImageBox(image_array=image_array, distance=0.01, stroke_width=1.5,depth_test=False)
        self.add(imageBox)
        self.add(axes)

        # math_tex2 = r"""
        #   \begin{bmatrix}
        #    -1&0&0\\0&1&0\\  0&0&1
        #   \end{bmatrix}
        # """
        # math_tex2 = MathTex(math_tex2).to_corner(corner=UR)
        # self.add_fixed_in_frame_mobjects(math_tex2)
        # self.play(Create(math_tex2))

        matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        # self.begin_ambient_camera_rotation(rate=1)
        self.wait(1)

class ThreeDReflection002(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}
=
\begin{bmatrix}1&0&0\\0&-1&0\\0&0&1\end{bmatrix}
\cdot
\begin{bmatrix}x\\y\\z\end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1).scale(0.7)
        self.add_fixed_in_frame_mobjects(math_tex1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))


        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-4, 4, 1], z_range=[-7, 7, 1],   x_length=14, y_length=8, z_length=14)
        axes.add(axes.get_axis_labels())
        self.play(Create(axes))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        imageBox = ImageBox(image_array=image_array, distance=0.01, stroke_width=1.5,depth_test=False)
        self.add(imageBox)
        self.add(axes)

        # math_tex2 = r"""
        #   \begin{bmatrix}
        #    -1&0&0\\0&1&0\\  0&0&1
        #   \end{bmatrix}
        # """
        # math_tex2 = MathTex(math_tex2).to_corner(corner=UR)
        # self.add_fixed_in_frame_mobjects(math_tex2)
        # self.play(Create(math_tex2))

        matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        # self.begin_ambient_camera_rotation(rate=1)
        self.wait(1)


class ThreeDReflection003(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}
=
\begin{bmatrix}1&0&0\\0&1&0\\0&0&-1\end{bmatrix}
\cdot
\begin{bmatrix}x\\y\\z\end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1).scale(0.7)
        self.add_fixed_in_frame_mobjects(math_tex1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))


        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],   x_length=14, y_length=14, z_length=8)
        axes.add(axes.get_axis_labels())
        self.play(Create(axes))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        imageBox = ImageBox(image_array=image_array, distance=0.01, stroke_width=1.5,depth_test=True)
        self.add(imageBox)
        self.add(axes)


        matrix = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, -1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        # self.begin_ambient_camera_rotation(rate=1)
        self.wait(1)


class ThreeDReflection004(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix}x'\\y'\\z'\end{bmatrix}
=
\begin{bmatrix}1&0&0\\0&1&0\\0&0&-1\end{bmatrix}
\cdot
\begin{bmatrix}x\\y\\z\end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1).scale(0.7)
        self.add_fixed_in_frame_mobjects(math_tex1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))


        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-4, 4, 1],   x_length=14, y_length=14, z_length=8)
        axes.add(axes.get_axis_labels())
        self.play(Create(axes))

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        imageBox = ImageBox(image_array=image_array, distance=0.01, stroke_width=1.5,depth_test=False)
        self.add(imageBox)
        self.add(axes)


        matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, -1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        # self.begin_ambient_camera_rotation(rate=1)
        self.wait(1)
# "disable_caching": True,
with tempconfig({"preview": True, "renderer": "opengl"}):
    ThreeDReflection004().render()
    exit(1)
