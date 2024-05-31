

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, ImageBox
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track
from PIL import Image



class ThreeDShear001(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix} x'\\y'\\z' \end{bmatrix}
=
\begin{bmatrix} 1& s&0\\ 0& 1&0\\0& 0&1 \end{bmatrix}
\cdot
\begin{bmatrix} x\\ y\\z \end{bmatrix}
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

        math_tex2 = r"""
          \begin{bmatrix}
           1&2&0\\0&1&0\\  0&0&1
          \end{bmatrix}
        """
        math_tex2 = MathTex(math_tex2).scale(0.7).to_corner(corner=UR)
        self.add_fixed_in_frame_mobjects(math_tex2)
        self.play(Create(math_tex2))

        matrix = np.array([
            [1, 2, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        # self.begin_ambient_camera_rotation(rate=1)
        self.wait(1)


class ThreeDShear002(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix} x'\\y'\\z' \end{bmatrix}
=
\begin{bmatrix} 1& 0&0\\ t& 1&0\\0& 0&1 \end{bmatrix}
\cdot
\begin{bmatrix} x\\ y\\z \end{bmatrix}
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

        math_tex2 = r"""
          \begin{bmatrix}
           1&0&0\\2&1&0\\  0&0&1
          \end{bmatrix}
        """
        math_tex2 = MathTex(math_tex2).scale(0.7).to_corner(corner=UR)
        self.add_fixed_in_frame_mobjects(math_tex2)
        self.play(Create(math_tex2))

        matrix = np.array([
            [1, 0, 0],
            [2, 1, 0],
            [0, 0, 1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        # self.begin_ambient_camera_rotation(rate=1)
        self.wait()


class ThreeDShear003(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix} x'\\y'\\z' \end{bmatrix}
=
\begin{bmatrix} 1& 0&s\\ 0& 1&t\\0& 0&1 \end{bmatrix}
\cdot
\begin{bmatrix} x\\ y\\z \end{bmatrix}
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

        math_tex2 = r"""
          \begin{bmatrix}
           1&0&2\\0&1&2\\  0&0&1
          \end{bmatrix}
        """
        math_tex2 = MathTex(math_tex2).scale(0.7).to_corner(corner=UR)
        self.add_fixed_in_frame_mobjects(math_tex2)
        self.play(Create(math_tex2))

        matrix = np.array([
            [1, 0, 2],
            [0, 1, 2],
            [0, 0, 1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T


        origin_points = imageBox.points.copy()

        self.play(ApplyMethod(imageBox.set_points, new_points))
        # self.begin_ambient_camera_rotation(rate=1)
        self.wait()

        self.move_camera(theta=0,phi=0)
        number_plane = NumberPlane()
        self.play(Create(number_plane))

        self.play(ApplyMethod(imageBox.set_points, origin_points))
        self.wait()

        self.play(ApplyMethod(imageBox.set_points, new_points))

        text= MarkupText("除Z 消除 z 轴")
        self.play(Create(text))
        #去掉z轴信息
        points = imageBox.points.copy()

        new_points = []
        for point in points:
            z = point[2]
            new_point = []
            new_point.append(point[0] / z)
            new_point.append(point[1] / z)
            new_point.append(1)
            new_points.append(new_point)
        new_points=np.array(new_points)
        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.wait()

class ThreeDShear004(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix} x'\\y'\\z' \end{bmatrix}
=
\begin{bmatrix} 1& 0&s\\ 0& 1&t\\0& 0&1 \end{bmatrix}
\cdot
\begin{bmatrix} x\\ y\\z \end{bmatrix}
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

        math_tex2 = r"""
          \begin{bmatrix}
           1&0&2\\0&1&2\\  0&0&1
          \end{bmatrix}
        """
        math_tex2 = MathTex(math_tex2).scale(0.7).to_corner(corner=UR)
        self.add_fixed_in_frame_mobjects(math_tex2)
        self.play(Create(math_tex2))

        matrix = np.array([
            [1, 0, 2],
            [0, 1, 2],
            [0, 0, 1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T


        origin_points = imageBox.points.copy()

        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.wait()

        self.play(ApplyMethod(imageBox.set_points, origin_points))
        self.wait()


        number_plane = NumberPlane(include_numbers=False,tips=False)
        self.play(Create(number_plane))

        text = MathTex("z=1",color=YELLOW).to_corner(UP)
        self.add_fixed_in_frame_mobjects(text)
        self.play(Create(text))

        origin_points[:,2]=1
        new_points=origin_points

        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.wait()

        new_points = matrix @ new_points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.move_camera(theta=0, phi=0)
        self.wait()


class ThreeDShear005(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
\begin{bmatrix} x'\\y'\\z' \end{bmatrix}
=
\begin{bmatrix} 1& 0&s\\ 0& 1&t\\0& 0&1 \end{bmatrix}
\cdot
\begin{bmatrix} x\\ y\\z \end{bmatrix}
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

        math_tex2 = r"""
          \begin{bmatrix}
           1&0&2\\0&1&2\\  0&0&1
          \end{bmatrix}
        """
        math_tex2 = MathTex(math_tex2).scale(0.7).to_corner(corner=UR)
        self.add_fixed_in_frame_mobjects(math_tex2)
        self.play(Create(math_tex2))

        matrix = np.array([
            [1, 0, 2],
            [0, 1, 2],
            [0, 0, 1]
        ])
        new_points = matrix @ imageBox.points.T
        new_points = new_points.T


        origin_points = imageBox.points.copy()

        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.wait()

        self.play(ApplyMethod(imageBox.set_points, origin_points))
        self.wait()


        number_plane = NumberPlane(include_numbers=False,tips=False)
        self.play(Create(number_plane))

        text = MathTex("z=2",color=YELLOW).to_corner(UP)
        self.add_fixed_in_frame_mobjects(text)
        self.play(Create(text))

        origin_points[:,2]=2
        new_points=origin_points

        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.wait()

        new_points = matrix @ new_points.T
        new_points = new_points.T

        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.move_camera(theta=0, phi=0)
        self.wait()

with tempconfig({"preview": True,"disable_caching": False, "renderer": "opengl"}):
    ThreeDShear005().render()
    exit(1)