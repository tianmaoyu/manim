import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, ImageBox
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track
from PIL import Image


class Translation001(ThreeDScene):
    def construct(self):
        latex_str1 = r"""
            \begin{bmatrix}  x'\\ y'\\  z' \end{bmatrix}
            =
            \begin{bmatrix} x\\ y\\ z \end{bmatrix}
            +
            \begin{bmatrix} x_1\\  y_1\\  z_1  \end{bmatrix}
         """

        math_tex1 = MathTex(latex_str1).scale(0.7)
        self.add_fixed_in_frame_mobjects(math_tex1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))

        # -------------start---------------
        self.set_camera_orientation(phi=75 * DEGREES, theta=7 * DEGREES)
        image = ImagePixelMobject("src/360-640-320.jpg", image_width=8, stroke_width=6.0)
        image.to_center()
        self.add(image)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-7, 7, 1],
                          x_length=14, y_length=10, z_length=14)
        self.add(axes)

        points = image.points

        # 平面转球面;
        # 1：平面尺寸映射：归一化；2. 归一化的长度 弧度化 映射，； 3： 再补充的半径就是极坐标
        # [r,phi,theta]
        spherical_points = np.empty_like(points)
        # 归一化，弧度化 映射
        width = 4
        spherical_points[:, 2] = PI * (points[:, 1] / width) - PI / 2
        spherical_points[:, 1] = PI * points[:, 0] / width
        spherical_points[:, 0] = 2  # 半径

        # 性能改进
        r = spherical_points[:, 0]
        theta = spherical_points[:, 1]
        phi = spherical_points[:, 2]

        x = r * np.cos(theta) * np.sin(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(phi)
        cartesian_points = np.stack((x, y, z), axis=-1)
        box_points = cartesian_points.copy()

        # 使用NumPy的广播和向量化操作来计算每个点的最大绝对值并进行归一化
        abs_values = np.abs(box_points)
        abs_max = np.max(abs_values, axis=1, keepdims=True)
        cube_points = box_points / abs_max
        image.points = cube_points
        # ------------end----------------

        mover_vector = np.array([2, 2, 2])
        vector = Vector(direction=mover_vector, color=YELLOW)
        vector.add(vector.coordinate_label(n_dim=3))
        self.play(Create(vector))

        lines = axes.get_lines_to_point(mover_vector)
        line = axes.get_line_from_axis_to_point(index=2, point=mover_vector)
        self.play(Create(lines), Create(line))

        new_points = image.points + mover_vector
        self.play(ApplyMethod(image.set_points, new_points))


class Translation002(ThreeDScene):

    def construct(self):

        latex_str1 = r"""
            \begin{bmatrix}  x'\\ y'\\  z' \end{bmatrix}
            =
            \begin{bmatrix} x\\ y\\ z \end{bmatrix}
            +
            \begin{bmatrix} x_1\\  y_1\\  z_1  \end{bmatrix}
         """
        math_tex1 = MathTex(latex_str1).scale(0.7)
        self.add_fixed_in_frame_mobjects(math_tex1)
        self.play(Create(math_tex1))
        self.play(math_tex1.animate.to_corner(UL))


        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-7, 7, 1],   x_length=14, y_length=14, z_length=14)
        axes.add(axes.get_axis_labels())
        self.play(Create(axes))

        # self.camera.light_source_position=[0,7,7]
        self.camera.light_source.move_to([7,7,7])

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        imageBox = ImageBox(image_array=image_array, distance=0.01, stroke_width=1.5,depth_test=False)
        self.add(imageBox)
        self.add(axes)

        mover_vector = np.array([2, 2, 2])
        vector = Vector(direction=mover_vector, color=YELLOW,depth_test=True)
        labes= vector.coordinate_label(n_dim=3, color=YELLOW)
        self.add_fixed_orientation_mobjects(labes)
        # vector.add()
        self.play(Create(vector),Create(labes))

        lines = axes.get_lines_to_point(mover_vector)
        line = axes.get_line_from_axis_to_point(index=2, point=mover_vector)
        self.play(Create(lines), Create(line))

        new_points = imageBox.points + mover_vector
        self.play(ApplyMethod(imageBox.set_points, new_points))
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(1)




# "disable_caching": True,
with tempconfig({"preview": True, "renderer": "opengl"}):
    Translation002().render()
    exit(1)
