import random
import time

from manim import *
from manim.mobject.opengl.opengl_cylinder import OpenGLCylinder
from manim.mobject.opengl.opengl_image_mobject import OpenGLImageMobject
from manim.mobject.opengl.opengl_point_image_mobject import ImagePixelMobject
from manim.mobject.opengl.opengl_shpere import OpenGLSphere
from manim.mobject.opengl.opengl_something import OpenGLCone, OpenGLLine3D
from manim.mobject.opengl.opengl_surface import OpenGLTexturedSurface, OpenGLSurface
import numpy as np
import sympy as sp
from manim.typing import Image
from PIL import Image


class NumpyImage(OpenGLPMobject):
    def __init__(self, image_array: np.ndarray, stroke_width=2.0, distance=0.025, **kwargs):
        super().__init__(**kwargs, stroke_width=stroke_width)

        # 构建三维坐标
        height, width, channel = image_array.shape
        assert channel == 4, "必须是r,g,b,a"
        points = np.zeros((height * width, 3))
        y_indices, x_indices = np.mgrid[0:height, 0:width]
        points[:, 0] = x_indices.flatten()  # x坐标
        points[:, 1] = y_indices.flatten()  # y坐标
        rgbas = image_array.reshape(-1, 4)

        # y轴反转和缩小- 一个坐标间隔为1
        points = points * distance * np.array([1, -1, 1])
        # 居中
        points += np.array([-width * distance / 2, height * distance / 2, 1])
        self.points = points
        self.rgbas = rgbas / 255

    def set_points(self, points: np.ndarray):
        self.points = points
        return self


class Prespective001(ThreeDScene):
    def construct(self):
        image = np.zeros((50, 50, 4), dtype=np.uint8)
        image[:, :, 0] = 255
        image[:, :, 3] = 255
        image_obj = NumpyImage(image_array=image, distance=0.05, stroke_width=2, depth_test=False)
        self.add(image_obj)

        matrix = np.array([
            [8.19902520e-01, 1.22854171e-01, -5.59166084e-01, 1.96241483e+06],
            [1.22854171e-01, 9.16194567e-01, 3.81437241e-01, -1.33864822e+06],
            [5.59166084e-01, -3.81437241e-01, 7.36097087e-01, -6.09287968e+06],
            [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]
        ])
        # matrix = np.array([
        #     [0.81990252, 0.12285417, -0.55916608, -26.03742335],
        #     [0.12285417, 0.91619457, 0.38143724, 38.16944558],
        #     [0.55916608, -0.38143724, 0.73609709, 0.],
        #     [0., 0., 0., 1.]
        # ])
        # matrix = np.array([
        #     [0.81990252, 0.12285417, -0.55916608, -26.03742335],
        #     [0.12285417, 0.91619457, 0.38143724, 38.16944558],
        #     [0.55916608, -0.38143724, 0.73609709, 0.],
        #     [0., 0., 0., 1.]
        # ])
        #
        # matrix = np.array([
        #     [0.81990252, 0.12285417, - 0.55916608, - 26.03742335],
        #     [0.12285417, 0.91619457, 0.38143724, 38.16944558],
        #     [0.55916608, - 0.38143724, 0.73609709, 50.],
        #     [0., 0., 0., 1.]
        # ])

        points = image_obj.points.copy()
        # 扩展一维，行相同
        ones = np.ones((points.shape[0], 1))
        points = np.hstack((points, ones))
        # 降维度不要追后列（如果没有转置不要最后一行）
        new_points = (matrix @ points.T).T

        new_points = new_points[:, :3]
        new_points = new_points - np.array([1962413, -1338647, -6092880])
        self.wait()
        self.play(ApplyMethod(image_obj.set_points, new_points * 0.2))


# 加载一张图片
class Prespective002(ThreeDScene):
    def construct(self):
        image_array = np.array(Image.open("src/3.jpeg").convert("RGBA"))

        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2,depth_test=False)
        # self.play(Create(image.scale(0.5)))
        self.add(image.scale(0.2))

        # image = np.zeros((50, 50, 4), dtype=np.uint8)
        # image[:, :, 0] = 255
        # image[:, :, 3] = 255
        # image_obj = NumpyImage(image_array=image, distance=0.05, stroke_width=2, depth_test=False)
        self.add(image)
        self.wait()

        matrix = np.array([
            [8.19902520e-01, 1.22854171e-01, -5.59166084e-01, 1.96241483e+06],
            [1.22854171e-01, 9.16194567e-01, 3.81437241e-01, -1.33864822e+06],
            [5.59166084e-01, -3.81437241e-01, 7.36097087e-01, -6.09287968e+06],
            [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]
        ])

        points = image.points.copy()
        # 扩展一维，行相同
        ones = np.ones((points.shape[0], 1))
        points = np.hstack((points, ones))
        # 降维度不要追后列（如果没有转置不要最后一行）
        new_points = (matrix @ points.T).T

        new_points = new_points[:, :3]
        # new_points = new_points - np.array([12624085, 2532779, 48])
        new_points = new_points - np.array([1962413, -1338647, -6092880])

        # new_points=(camera1_init@new_points.T).T
        image.set_points(new_points)
        self.wait()
        # self.set_camera_orientation(theta=45*DEGREES,phi=65*DEGREES)
        # self.begin_ambient_camera_rotation(rate=2)
        # self.wait(1)
        # self.play(ApplyMethod(image.set_points, new_points))


def image_to_camera_test_v2():
    pixel = 1.6 / 1000_000
    x_range = np.arange(4000)
    y_range = np.arange(3000)
    # 创建网格，这将生成所有可能的(x, y)组合
    X, Y = np.meshgrid(y_range - 1500, x_range - 2000)
    # 将网格转换为所需的形式，并应用像素大小
    c_y = X * pixel
    c_z = Y * pixel
    # 添加常数c_x
    c_x = np.full(c_y.shape, 0.0044)
    # 将c_x, c_y, c_z堆叠成一个3D数组
    points = np.dstack((c_x, c_y, c_z))
    # 转换形状以获得一个点列表
    points = points.reshape(-1, 3)
    return points


class Prespective003(ThreeDScene):
    # 全部转到 相机下
    def image_to_camera( x: int, y: int) -> np.ndarray:
        pixel = 1.6 / 1000_000
        c_x = 0.0045
        c_y = (x - 2000 / 2) * pixel
        c_z = (y - 1500 / 2) * pixel
        return np.array([c_x, c_y, c_z])
    def construct(self):


        image_array = np.array(Image.open("src/3-mini.jpeg").convert("RGBA"))

        image = NumpyImage(image_array=image_array, distance=0.01, stroke_width=2, depth_test=False)

        self.add(image.scale(0.2))

        # image = np.zeros((50, 50, 4), dtype=np.uint8)
        # image[:, :, 0] = 255
        # image[:, :, 3] = 255
        # image_obj = NumpyImage(image_array=image, distance=0.05, stroke_width=2, depth_test=False)
        self.add(image)
        self.wait()
        # 相对变换
        matrix = np.array([
            [8.19902520e-01, 1.22854171e-01, -5.59166084e-01, 1.96241483e+06],
            [1.22854171e-01, 9.16194567e-01, 3.81437241e-01, -1.33864822e+06],
            [5.59166084e-01, -3.81437241e-01, 7.36097087e-01, -6.09287968e+06],
            [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]
        ])
        matrix = np.array([
            [8.19902520e-01, 1.22854171e-01, - 5.59166084e-01, 1.45865060e+07],
            [1.22854171e-01, 9.16194567e-01, 3.81437241e-01, 1.19411985e+06],
            [5.59166084e-01, - 3.81437241e-01, 7.36097087e-01, - 6.09287968e+06],
            [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]
        ])

        # points = image_to_camera_test_v2()*10000

        points = image.points.copy()
        # 扩展一维，行相同
        ones = np.ones((points.shape[0], 1))
        points = np.hstack((points, ones))
        # 降维度不要追后列（如果没有转置不要最后一行）
        new_points = (matrix @ points.T).T
        new_points = new_points[:, :3]
        # new_points = new_points - np.array([1962413, -1338647, -6092880])
        new_points = new_points - np.array([14586503  , 1194121 , -6092880])
        # z= new_points[:,2]
        # new_points[:,0]= new_points[:,0]/ z
        # new_points[:, 1] = new_points[:, 1] / z
        new_points[:, 2] = 1
        image.set_points(new_points)
        self.wait()

with tempconfig({"preview": True, "renderer": "opengl"}):
    Prespective003().render()
    exit(1)
