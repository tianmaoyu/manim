import time

from manim import *
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject, NumpyImage, ImageBox
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
from rich.progress import track
from PIL import Image

# 三点共线，已经知道 O,P 坐标 以及 G（x,y,z）坐标中的z值，计算 x,y 并返回G
def point_from_collinearity(O: dict, P: dict, z: float) -> dict:
    if P[2] - O[2] == 0 or z - P[2] == 0:
        return (float('inf'), float('inf'), z)

    λ = (P[2] - O[2]) / (z - P[2])
    # λ 为负数时 todo
    x = (P[0] - O[0]) / λ + P[0]
    y = (P[1] - O[1]) / λ + P[1]
    return (x, y, z)


"""
theta: 0-2PI  0-360°
phi: 3/4PI - PI  120°-180°
假设：new_r= 2r 
坐标z: 映射到 z=-r 平面上"""


class DemoSkybox007(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=7 * DEGREES)

        image = ImagePixelMobject("src/360-640-320.jpg", image_width=8, stroke_width=6.0)
        image.to_center()
        self.add(image)
        axes = ThreeDAxes(include_numbers=False,x_range=[-7, 7, 1],y_range=[-5, 5, 1],z_range=[-7, 7, 1],x_length=14, y_length=10,z_length=14)
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
        box_points= cartesian_points.copy()

        # 使用NumPy的广播和向量化操作来计算每个点的最大绝对值并进行归一化
        abs_values = np.abs(box_points)
        abs_max = np.max(abs_values, axis=1, keepdims=True)
        cube_points = box_points / abs_max
        image.points=cube_points


        mover_vector = np.array([2, 2, 2])
        vector = Vector(direction=mover_vector,color=YELLOW)
        vector.add(vector.coordinate_label(n_dim=3))
        self.play(Create(vector))

        lines=axes.get_lines_to_point(mover_vector)
        line=axes.get_line_from_axis_to_point(index=2,point=mover_vector)
        self.play(Create(lines),Create(line))

        new_points = image.points + mover_vector
        self.play(ApplyMethod(image.set_points, new_points))






class AddImageToBox(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-7, 7, 1],   x_length=14, y_length=10, z_length=14)
        axes.add(axes.get_axis_labels())

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2)
        self.play(Create(image),Create(axes))

        original_points=image.points.copy()
        original_rgbas = image.rgbas.copy()

        offset = image.width /2

        z_in = image.points.copy() + np.array([0, 0, -offset])
        points = np.append(original_points, z_in, axis=0)
        rgbas = np.append(original_rgbas, original_rgbas, axis=0)

        left =rotation_matrix(90*DEGREES,axis=UP) @ image.points.copy().T
        left=left.T+np.array([-offset,0,0])
        points= np.append(points,left,axis=0)
        rgbas = np.append(rgbas, original_rgbas,axis=0)

        up = rotation_matrix(90 * DEGREES, axis=RIGHT) @ image.points.copy().T
        up = up.T + np.array([0, offset, 0])
        points = np.append(points, up, axis=0)
        rgbas = np.append(rgbas, original_rgbas, axis=0)

        right = rotation_matrix(90 * DEGREES, axis=UP) @ image.points.copy().T
        right = right.T + np.array([offset, 0, 0])
        points = np.append(points, right, axis=0)
        rgbas = np.append(rgbas, original_rgbas, axis=0)

        down = rotation_matrix(90 * DEGREES, axis=RIGHT) @ image.points.copy().T
        down = down.T + np.array([0, -offset, 0])
        points = np.append(points, down, axis=0)
        rgbas = np.append(rgbas, original_rgbas, axis=0)

        z_out = image.points.copy() + np.array([0, 0, offset])
        points = np.append(points, z_out, axis=0)
        rgbas = np.append(rgbas, original_rgbas, axis=0)

        image.points=points
        image.rgbas=rgbas
        # self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(1)


class AddImageToBox002(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-5, 5, 1], z_range=[-7, 7, 1],   x_length=14, y_length=10, z_length=14)
        axes.add(axes.get_axis_labels())

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        imageBox = ImageBox(image_array=image_array, distance=0.01, stroke_width=2)
        self.add(imageBox)

        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(1)


class lightSource001(ThreeDScene):

    def construct(self):
        # obj = self.camera.light_source
        # self.camera.light_source.move_to([5, -10, 10])

        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        axes = ThreeDAxes(include_numbers=False, x_range=[-7, 7, 1], y_range=[-7, 7, 1], z_range=[-7, 7, 1],   x_length=14, y_length=14, z_length=14)
        axes.add(axes.get_axis_labels())
        self.add(axes)

        image_array = np.array(Image.open("src/test.jpg").convert("RGBA"))
        imageBox = ImageBox(image_array=image_array, distance=0.01, stroke_width=1.5,depth_test=False)
        self.add(imageBox)


        # animate= self.camera.light_source.animate.move_to([0, 0, 10])
        # self.play(animate,run_time=2)

        self.begin_ambient_camera_rotation(rate=1)
        self.wait(2)


def point_from_collinearity_np(light, points: np.ndarray, z):
    """
    light ，灯光点
    points 需要投影的数据，
    z 值
    """
    λ = (points[:, 2] - light[2]) / (z- points[:, 2] )
    x = (points[:, 0] - light[0]) / λ + points[:, 0]
    y = (points[:, 1] - light[1]) / λ + points[:, 1]
    z = np.full_like(x, z)
    return np.column_stack((x, y, z))


# "disable_caching": True,
with tempconfig({"preview": True, "renderer": "opengl"}):
    lightSource001().render()
    exit(1)
